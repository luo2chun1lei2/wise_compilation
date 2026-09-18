#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GitHub AI 热门项目 Top10 试跑脚本（T3 调查 + 数据流端到端验证）.

数据流（ai/design.md §1，ADR-0011）：获取材料 → 获取摘要 → 翻译判定 → 存库 → 生成 result 文档。
- 采集：GitHub Search API（官方 REST，ADR-0012）
- 摘要：级联提取（description → README 文首 TL;DR/首段 → 截断），纯工具
- 翻译：中文跳过；外文 ≤5000B 走 GLM（ADR-0010），超限/失败保原文
- 存库：SQLite data/wise.db（只存链接+摘要）
- 输出：result/github-ai-top10-<date>.md（排名+简介，不发布）
"""
import argparse
import json
import re
import sqlite3
import sys
import time
from datetime import date, datetime, timedelta
from html import unescape
from pathlib import Path

import requests
import yaml

try:
    import feedparser
except ImportError:
    feedparser = None

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / "ai" / "secret.md"
SOURCES_PATH = ROOT / "config" / "sources.yaml"
DATA_DIR = ROOT / "data"
RESULT_DIR = ROOT / "result"
DB_PATH = DATA_DIR / "wise.db"
TRENDING_URL = "https://github.com/trending"

MAX_TRANSLATE_BYTES = 5000   # ADR-0010 翻译上限（UTF-8 字节）
MIN_DESC_BYTES = 80          # 描述过短时从 README 文首补充摘要
HEAD_SUMMARY_BYTES = 1500    # README 文首提取的摘要上限
FETCH_INTERVAL = 1.0         # 对 github.com 的请求间隔（ADR-0006 礼貌抓取）
DEFAULT_QUERY = "topic:artificial-intelligence stars:>500 pushed:>{week}"

# 运行统计（成本项）：token 数来自 GLM 响应的 usage 字段，精确值
STATS = {"gh_api": 0, "zhihu_api": 0, "csdn_api": 0, "rss_api": 0, "hn_api": 0,
         "llm_calls": 0, "prompt_tokens": 0,
         "completion_tokens": 0, "total_tokens": 0}

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
ZHIHU_HOT_URL = "https://api.zhihu.com/topstory/hot-list"
# 知乎热榜 AI 过滤关键词（sources.yaml 的 keywords 可追加，ADR-0014）
AI_KEYWORDS = ["AI", "人工智能", "大模型", "LLM", "GPT", "ChatGPT", "智能体", "Agent",
               "深度学习", "机器学习", "DeepSeek", "豆包", "文心", "通义", "Kimi",
               "Claude", "OpenAI", "Gemini", "Sora", "算力", "AGI", "神经网络",
               "AIGC", "具身智能", "RAG", "Scaling"]


def load_secret():
    kv = {}
    for line in SECRET_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*([A-Z_]+):\s*(\S.*)", line)
        if m:
            kv[m.group(1)] = m.group(2).strip()
    return kv


def cjk_ratio(text):
    if not text:
        return 0.0
    cjk = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
    return cjk / max(len(text), 1)


def resolve_query(query):
    """把查询里的 now-Nd 占位符解析为具体日期（如 now-7d → 2026-09-09）。"""
    return re.sub(r"now-(\d+)d",
                  lambda m: (date.today() - timedelta(days=int(m.group(1)))).strftime("%Y-%m-%d"),
                  query)


def load_source_entry(name):
    """从 config/sources.yaml 读取指定源的配置。"""
    data = yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8"))
    for s in data.get("sources") or []:
        if s.get("name") == name and s.get("enabled", True):
            return s
    raise SystemExit("在 %s 中未找到启用的源 %r" % (SOURCES_PATH, name))


def fetch_zhihu_columns(columns, per_column, rank_by):
    """知乎专栏文章流（mode: column，ADR-0015）。

    每个专栏取最新 per_column 篇（sort_by=created），合并后按 rank_by 排序：
    updated=发布时间新在前 | voteup=点赞数高在前（热度排名）。
    注意：专栏 meta 的 updated 字段过期不可信，以文章列表实际日期为准。
    """
    repos = []
    for slug in columns:
        meta = {}
        try:
            r = requests.get("https://www.zhihu.com/api/v4/columns/%s" % slug,
                             headers={"User-Agent": UA}, timeout=30)
            r.raise_for_status()
            STATS["zhihu_api"] += 1
            meta = r.json()
        except Exception as exc:
            print("  [warn] 专栏 %s meta: %s" % (slug, exc), file=sys.stderr)
        col_name = meta.get("title") or slug
        try:
            r = requests.get("https://www.zhihu.com/api/v4/columns/%s/articles" % slug,
                             params={"limit": per_column, "sort_by": "created"},
                             headers={"User-Agent": UA}, timeout=30)
            r.raise_for_status()
            STATS["zhihu_api"] += 1
        except Exception as exc:
            print("  [warn] 专栏 %s articles: %s" % (slug, exc), file=sys.stderr)
            time.sleep(FETCH_INTERVAL)
            continue
        for it in r.json().get("data", []):
            created = it.get("created")
            repos.append({
                "full_name": it.get("title", "").strip(),
                "html_url": it.get("url", ""),
                "description": (it.get("excerpt") or "").strip(),
                "stargazers_count": it.get("voteup_count", 0),
                "language": None,
                "topics": [],
                "pushed_at": datetime.fromtimestamp(created).strftime("%Y-%m-%dT%H:%M:%S") if created else "",
                "zhihu_meta": {"voteup": it.get("voteup_count", 0),
                               "comments": it.get("comment_count", 0),
                               "column": col_name},
                "no_readme": True,
            })
        time.sleep(FETCH_INTERVAL)
    repos.sort(key=lambda x: x["pushed_at"], reverse=(rank_by != "voteup"))
    if rank_by == "voteup":
        repos.sort(key=lambda x: x["stargazers_count"], reverse=True)
    return [r for r in repos if r["full_name"] and r["html_url"]]


def fetch_rss(url, limit):
    """RSS/Atom 采集（type: rss，ADR-0020 准入：正规订阅源，取最新 N 条）。

    返回 repo 形条目：标题/链接/发布时间/摘要（summary 去 HTML 标签，feed 级）。
    """
    if feedparser is None:
        raise RuntimeError("未安装 feedparser（pip3 install --user feedparser）")
    r = requests.get(url, headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    STATS["rss_api"] += 1
    d = feedparser.parse(r.content)
    feed_title = (d.feed.get("title") or url).strip()
    repos = []
    for e in d.entries[:limit]:
        title = (e.get("title") or "").strip()
        link = (e.get("link") or "").strip()
        if not (title and link):
            continue
        summary = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                             e.get("summary") or e.get("description") or "")).strip()
        published = ""
        raw = e.get("published") or e.get("updated") or ""
        if raw:
            try:
                from email.utils import parsedate_to_datetime
                published = parsedate_to_datetime(raw).strftime("%Y-%m-%dT%H:%M:%S")
            except Exception:
                published = raw[:19]
        repos.append({
            "full_name": title,
            "html_url": link,
            "description": summary,
            "stargazers_count": 0,
            "language": None,
            "topics": [],
            "pushed_at": published,
            "zhihu_meta": None,
            "rss_meta": {"feed": True, "feed_title": feed_title},
            "en_article": True,
            "no_readme": True,
        })
    return repos


def fetch_hn(limit):
    """Hacker News 热点榜（type: hn，ADR-0020 排名语义：front_page 按 points 排序）。

    官方 Algolia API，无需凭据；条目自带 points/评论数。
    """
    r = requests.get("https://hn.algolia.com/api/v1/search",
                     params={"tags": "front_page", "hitsPerPage": limit},
                     headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    STATS["hn_api"] += 1
    repos = []
    for h in r.json().get("hits", []):
        title = (h.get("title") or "").strip()
        if not title:
            continue
        url = (h.get("url") or "https://news.ycombinator.com/item?id=%s"
               % h.get("objectID", "")).strip()
        desc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
                                          h.get("story_text") or "")).strip()
        repos.append({
            "full_name": title,
            "html_url": url,
            "description": desc,
            "stargazers_count": h.get("points") or 0,
            "language": None,
            "topics": [],
            "pushed_at": (h.get("created_at") or "")[:19],
            "zhihu_meta": {"voteup": h.get("points") or 0,
                           "comments": h.get("num_comments") or 0,
                           "column": "Hacker News"},
            "en_article": True,
            "no_readme": True,
        })
    repos.sort(key=lambda x: x["zhihu_meta"]["voteup"], reverse=True)
    return repos


def fetch_csdn_search(query, tm, size, days):
    """CSDN 文章搜索（type: csdn, mode: search，ADR-0019）。

    so.csdn.net 公开接口：q=关键词、t=blog、tm=时间窗（1=当天，2/3=更宽），
    返回 标题/链接/created_at/description/点赞。days 为客户端二次过滤（如 3 天内）。
    """
    r = requests.get("https://so.csdn.net/api/v3/search",
                     params={"q": query, "t": "blog", "p": 1, "tm": tm, "size": size, "v": 3},
                     headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    STATS["csdn_api"] += 1
    cutoff = date.today() - timedelta(days=days)
    repos = []
    for it in r.json().get("result_vos", []):
        created = str(it.get("created_at") or "")[:10]
        try:
            if datetime.strptime(created, "%Y-%m-%d").date() < cutoff:
                continue
        except ValueError:
            pass
        title = re.sub(r"</?em>", "", str(it.get("title") or "")).strip()
        url = re.sub(r"\?.*$", "", str(it.get("url") or ""))
        if not (title and "/article/details/" in url):
            continue
        repos.append({
            "full_name": title,
            "html_url": url,
            "description": re.sub(r"</?em>", "", str(it.get("description") or "")).strip(),
            "stargazers_count": 0,
            "language": None,
            "topics": [],
            "pushed_at": created,
            "zhihu_meta": {"voteup": it.get("digg") or 0,
                           "comments": it.get("comment") or 0,
                           "column": it.get("author") or ""},
            "no_readme": True,
        })
    return repos


def fetch_zhihu_hot(limit, ai_filter, extra_kws):
    """知乎全站热榜（mode: hot-list，ADR-0014）。

    无需登录；target 自带 标题/excerpt 摘要/回答数/创建时间，detail_text 为热度。
    ai_filter=True 时仅保留标题命中 AI 关键词的条目（话题级接口需登录，未采用）。
    """
    r = requests.get(ZHIHU_HOT_URL, params={"limit": limit, "domain": "www.zhihu.com"},
                     headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    STATS["zhihu_api"] += 1
    kws = set(k.lower() for k in AI_KEYWORDS) | set(k.lower() for k in extra_kws)
    repos = []
    for it in r.json().get("data", []):
        t = it.get("target") or {}
        title = t.get("title", "").strip()
        if not title:
            continue
        if ai_filter and not any(k in title.lower() for k in kws):
            continue
        created = t.get("created")
        repos.append({
            "full_name": title,
            "html_url": "https://www.zhihu.com/question/%s" % t.get("id"),
            "description": (t.get("excerpt") or "").strip() or it.get("detail_text", ""),
            "stargazers_count": 0,
            "language": None,
            "topics": [],
            "pushed_at": datetime.fromtimestamp(created).strftime("%Y-%m-%dT%H:%M:%S") if created else "",
            "zhihu_meta": {"heat": it.get("detail_text", ""), "answers": t.get("answer_count", 0)},
            "no_readme": True,
        })
    return repos


def gh_headers(token, raw=False):
    h = {"Accept": "application/vnd.github.raw" if raw else "application/vnd.github+json"}
    if token:
        h["Authorization"] = "Bearer " + token
    return h


# ---------- 步骤 1：获取材料 ----------

def search_repos(query, per_page, token):
    url = "https://api.github.com/search/repositories"
    STATS["gh_api"] += 1
    r = requests.get(url, params={"q": query, "sort": "stars", "order": "desc",
                                  "per_page": per_page},
                     headers=gh_headers(token), timeout=30)
    r.raise_for_status()
    return r.json()["items"]


def fetch_readme(full_name, token):
    url = "https://api.github.com/repos/%s/readme" % full_name
    STATS["gh_api"] += 1
    r = requests.get(url, headers=gh_headers(token, raw=True), timeout=30)
    if r.status_code == 404:
        return ""
    r.raise_for_status()
    return r.text


def fetch_trending(since):
    """解析 GitHub Trending 页面（mode: trending，ADR-0013）。

    每行自带：仓库、描述、语言、总 star、本期增量（如 "16,763 stars this month"）。
    解析 0 行视为页面改版，抛错由上层按源隔离处理。
    """
    for attempt in (1, 2, 3):
        try:
            r = requests.get(TRENDING_URL, params={"since": since},
                             headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
            r.raise_for_status()
            break
        except requests.RequestException as exc:
            if attempt == 3:
                raise
            print("  [warn] trending attempt%d: %s" % (attempt, exc), file=sys.stderr)
            time.sleep(5)
    STATS["gh_api"] += 1
    repos = []
    for block in r.text.split('<article class="Box-row">')[1:]:
        m = re.search(r'<h2[^>]*>.*?href="/([^/"]+)/([^"]+)"', block, re.S)
        if not m:
            continue
        owner, name = m.group(1), m.group(2)
        dm = re.search(r'<p class="col-9[^"]*">(.*?)</p>', block, re.S)
        desc = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", dm.group(1)))).strip() if dm else ""
        lm = re.search(r'itemprop="programmingLanguage">([^<]+)', block)
        sm = re.search(r'href="/[^/]+/[^/]+/stargazers"[^>]*>\s*<svg.*?</svg>\s*([\d,]+)', block, re.S)
        pm = re.search(r"([\d,]+) stars (this month|this week|today)", block)
        repos.append({
            "full_name": "%s/%s" % (owner, name),
            "html_url": "https://github.com/%s/%s" % (owner, name),
            "description": desc,
            "stargazers_count": int(sm.group(1).replace(",", "")) if sm else 0,
            "language": lm.group(1).strip() if lm else None,
            "topics": [],
            "pushed_at": "",
            "trending_delta": ("%s stars %s" % (pm.group(1), pm.group(2))) if pm else "",
        })
    if not repos:
        raise RuntimeError("Trending 页面解析到 0 行，GitHub 可能改版（ADR-0013 风险项）")
    return repos


# ---------- 步骤 2：获取摘要（级联，纯工具） ----------

def extract_head_summary(readme_md, limit=HEAD_SUMMARY_BYTES):
    """从 README 文首提取摘要：TL;DR/Abstract 节优先，否则首个实质段落组。"""
    if not readme_md:
        return ""
    lines, buf, marker_hit = [], [], False
    marker = re.compile(r"(tl;?dr|abstract|about|简介|摘要)", re.I)
    for raw in readme_md.splitlines():
        line = re.sub(r"<[^>]+>", " ", raw).strip()          # 去 HTML 标签/徽章
        line = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", line).strip()  # 去图片
        if not line or line.startswith(("[!", "<", "---")):
            continue
        is_head = line.startswith("#")
        if is_head and marker.search(line):
            marker_hit, buf = True, []
            continue
        if is_head:
            if marker_hit and buf:
                break
            continue
        if line.startswith(("[", "|", "```")):
            continue
        buf.append(line)
        if len("\n".join(buf).encode("utf-8")) >= limit:
            break
    return "\n".join(buf)[:limit * 2]


def summary_cascade(repo, token):
    """级联：description → README 文首 → 空串（no_readme 的源跳过 README）。返回 (summary, source)。"""
    desc = (repo.get("description") or "").strip()
    if repo.get("no_readme") or len(desc.encode("utf-8")) >= MIN_DESC_BYTES:
        return desc, "feed"
    time.sleep(FETCH_INTERVAL)
    try:
        head = extract_head_summary(fetch_readme(repo["full_name"], token))
    except Exception as exc:
        print("  [warn] readme %s: %s" % (repo["full_name"], exc), file=sys.stderr)
        head = ""
    if head:
        return (desc + "\n" + head).strip() if desc else head, "readme_head"
    return desc, "feed"


# ---------- 步骤 3：翻译判定（LLM + 上限路由，ADR-0010） ----------

def translate(text, secret):
    if not text:
        return text, "empty"
    if cjk_ratio(text) > 0.25:
        return text, "zh-skip"
    if len(text.encode("utf-8")) > MAX_TRANSLATE_BYTES:
        return text, "oversize-keep-original"
    base = secret.get("LLM_BASE_URL", "").rstrip("/")
    key, model = secret.get("LLM_API_KEY"), secret.get("LLM_MODEL")
    if not (base and key and model):
        return text, "no-llm-config"
    payload = {
        "model": model, "temperature": 0.2, "max_tokens": 4000,
        "messages": [
            {"role": "system", "content": "你是技术翻译引擎。把用户给的英文资料译成简体中文，"
                                           "保留专有名词与代码名，只输出译文。"},
            {"role": "user", "content": text},
        ],
    }
    for attempt in (1, 2):
        try:
            r = requests.post(base + "/chat/completions",
                              headers={"Authorization": "Bearer " + key,
                                       "Content-Type": "application/json"},
                              json=payload, timeout=120)
            r.raise_for_status()
            body = r.json()
            out = body["choices"][0]["message"].get("content", "").strip()
            usage = body.get("usage") or {}
            STATS["llm_calls"] += 1
            STATS["prompt_tokens"] += usage.get("prompt_tokens", 0)
            STATS["completion_tokens"] += usage.get("completion_tokens", 0)
            STATS["total_tokens"] += usage.get("total_tokens", 0)
            if out:
                return out, "llm"
        except Exception as exc:
            print("  [warn] llm attempt%d: %s" % (attempt, exc), file=sys.stderr)
            time.sleep(3)
    return text, "translate-failed"


def translate_article(title, summary, secret):
    """英文文章源（RSS/HN）：标题+摘要合并一次调用翻译（ADR-0010「标题始终翻译」，不增调用数）。

    返回 (title_zh, summary_zh, lang)；解析失败时回退为仅译摘要、标题保留原文。
    """
    if cjk_ratio(title) > 0.25 and (not summary or cjk_ratio(summary) > 0.25):
        return title, summary, "zh-skip"
    if len((title + (summary or "")).encode("utf-8")) > MAX_TRANSLATE_BYTES:
        zh, lang = translate(summary, secret)
        return title, zh, lang + "|超限保原文"
    base = secret.get("LLM_BASE_URL", "").rstrip("/")
    key, model = secret.get("LLM_API_KEY"), secret.get("LLM_MODEL")
    if not (base and key and model):
        return title, summary, "no-llm-config"
    payload = {
        "model": model, "temperature": 0.2, "max_tokens": 4000,
        "messages": [
            {"role": "system", "content": "你是技术翻译引擎，把英文资讯译成简体中文，保留专有名词。"
                                           "严格按格式：第一行只输出标题译文；第二行只输出===；之后输出摘要译文。"},
            {"role": "user", "content": "标题：%s\n\n摘要：%s" % (title, summary or "（无）")},
        ],
    }
    for attempt in (1, 2):
        try:
            r = requests.post(base + "/chat/completions",
                              headers={"Authorization": "Bearer " + key,
                                       "Content-Type": "application/json"},
                              json=payload, timeout=120)
            r.raise_for_status()
            body = r.json()
            out = body["choices"][0]["message"].get("content", "").strip()
            usage = body.get("usage") or {}
            STATS["llm_calls"] += 1
            STATS["prompt_tokens"] += usage.get("prompt_tokens", 0)
            STATS["completion_tokens"] += usage.get("completion_tokens", 0)
            STATS["total_tokens"] += usage.get("total_tokens", 0)
            parts = out.split("===")
            if len(parts) == 2 and parts[0].strip() and parts[1].strip():
                t_zh = re.sub(r"^标题[：:]\s*", "", parts[0]).strip()
                s_zh = re.sub(r"^摘要[：:]\s*", "", parts[1]).strip()
                if s_zh in ("（无）", "(无)", "无"):
                    s_zh = ""
                if t_zh:
                    return t_zh, s_zh or summary, "llm"
        except Exception as exc:
            print("  [warn] llm-article attempt%d: %s" % (attempt, exc), file=sys.stderr)
            time.sleep(3)
    zh, lang = translate(summary, secret)   # 回退：仅摘要
    return title, zh, lang + "|title-keep"


# ---------- 步骤 4：存库 ----------

def init_db():
    DATA_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS sources(
      id INTEGER PRIMARY KEY, name TEXT UNIQUE, type TEXT, url TEXT,
      last_fetch_at TEXT, fail_count INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS items(
      id INTEGER PRIMARY KEY, source_id INTEGER, url_norm TEXT UNIQUE,
      title TEXT, url TEXT, summary TEXT, summary_zh TEXT, summary_from TEXT,
      lang TEXT, stars INTEGER, published_at TEXT, collected_at TEXT,
      status TEXT DEFAULT 'new', meta TEXT);
    CREATE TABLE IF NOT EXISTS runs(
      id INTEGER PRIMARY KEY, kind TEXT, started_at TEXT, finished_at TEXT,
      status TEXT, stats TEXT, error TEXT);
    """)
    return conn


def store(conn, entries):
    conn.execute("INSERT OR IGNORE INTO sources(name,type,url) VALUES(?,?,?)",
                 ("github-ai-top10", "github", "https://api.github.com/search"))
    src_id = conn.execute("SELECT id FROM sources WHERE name='github-ai-top10'").fetchone()[0]
    n = 0
    for e in entries:
        cur = conn.execute(
            "INSERT OR IGNORE INTO items(source_id,url_norm,title,url,summary,summary_zh,"
            "summary_from,lang,stars,published_at,collected_at,meta) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (src_id, e["url_norm"], e["title"], e["url"], e["summary"], e["summary_zh"],
             e["summary_from"], e["lang"], e["stars"], e["published_at"],
             e["collected_at"], json.dumps(e["meta"], ensure_ascii=False)))
        n += cur.rowcount
    conn.commit()
    return n


# ---------- 步骤 5：生成 result 文档 ----------

def cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def render_md(entries, query, out_path, stats, elapsed, label=None):
    is_trending = "github.com/trending" in query
    is_zhihu_col = bool(entries) and all("voteup" in e["meta"] for e in entries)
    is_zhihu = bool(entries) and all("heat" in e["meta"] for e in entries)
    day = date.today().strftime("%Y-%m-%d")
    is_csdn = "csdn.net" in query
    is_hn = "hn.algolia" in query
    is_feed = bool(entries) and all(e["meta"].get("feed") for e in entries)
    if is_hn:
        title = "Hacker News 热点榜（%s）" % day
    elif is_feed:
        feed_title = (entries[0]["meta"].get("feed_title") or "RSS 资讯")[:20]
        title = "%s（%s）" % (feed_title, day)
    elif is_zhihu_col:
        title = ("CSDN AI 文章榜（%s）" % day) if is_csdn else ("知乎 AI 专栏榜（%s）" % day)
    elif is_zhihu:
        title = "知乎热榜 AI 筛选（%s）" % day
    elif label:
        title = "GitHub 热门项目（%s · %s）" % (label, day)
    else:
        title = "GitHub AI 热门项目榜（%s）" % day
    if is_hn:
        data_src = "Hacker News 官方 Algolia API（front_page，按 points 排名）"
    elif is_feed:
        data_src = "RSS 订阅（%s，最新 N 条）" % query.replace("RSS：", "")[:60]
    elif is_zhihu_col:
        data_src = ("CSDN 搜索接口（so.csdn.net/api/v3，时间窗过滤）" if is_csdn
                    else "知乎专栏文章 API（api/v4/columns，无需登录）")
    elif is_zhihu:
        data_src = "知乎热榜 API（api.zhihu.com，无需登录，AI 关键词过滤）"
    elif is_trending:
        data_src = "GitHub Trending 页面解析（本期 star 增量排序）"
    else:
        data_src = "GitHub Search API（官方接口，按 star 数降序）"
    lines = [
        "# " + title, "",
        "- 生成时间：%s" % datetime.now().strftime("%Y-%m-%d %H:%M"),
        "- 数据来源：%s" % data_src,
        "- 查询条件：`%s`" % query,
        "- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布", "",
    ]
    has_delta = any(e["meta"].get("period_delta") for e in entries)

    def disp_title(e):
        t = e.get("title_disp") or e["title"]
        return t if len(t) <= 36 else t[:35] + "…"

    if is_feed:
        lines += ["| 排名 | 文章 | 发布时间 | 简介 |", "|" + "---|" * 4]
        for i, e in enumerate(entries, 1):
            lines.append("| %d | [%s](%s) | %s | %s |" % (
                i, cell(disp_title(e)), e["url"], (e["published_at"][:16] or "-").replace("T", " "),
                cell(e["summary_zh"].split("\n")[0][:110])))
    elif is_zhihu_col:
        def _int(x):
            try:
                return int(x)
            except (TypeError, ValueError):
                return 0
        lines += ["| 排名 | 文章 | 专栏 | 赞 | 评论 | 中文简介 |", "|" + "---|" * 6]
        for i, e in enumerate(entries, 1):
            m = e["meta"]
            lines.append("| %d | [%s](%s) | %s | %s | %s | %s |" % (
                i, cell(disp_title(e)), e["url"], cell(m.get("column") or "-"),
                format(_int(m.get("voteup")), ","), format(_int(m.get("comments")), ","),
                cell(e["summary_zh"].split("\n")[0][:100])))
    elif is_zhihu:
        lines += ["| 排名 | 话题 | 热度 | 回答 | 中文简介 |", "|" + "---|" * 5]
        for i, e in enumerate(entries, 1):
            ans = e["meta"].get("answers") or 0
            lines.append("| %d | [%s](%s) | %s | %s | %s |" % (
                i, cell(disp_title(e)), e["url"], e["meta"].get("heat") or "-",
                format(ans, ","), cell(e["summary_zh"].split("\n")[0][:120])))
    else:
        lines += ["| 排名 | 项目 | Stars | %s语言 | 中文简介 |" % ("本期新增 | " if has_delta else ""),
                  "|" + "---|" * (6 if has_delta else 5)]
        for i, e in enumerate(entries, 1):
            brief = e["summary_zh"].split("\n")[0][:120]
            lang_col = e["meta"].get("language") or "-"
            if has_delta:
                delta = (e["meta"].get("period_delta", "")
                         .replace(" stars this month", "★/月")
                         .replace(" stars this week", "★/周")
                         .replace(" stars today", "★/日")) or "-"
                lines.append("| %d | [%s](%s) | %s | %s | %s | %s |" % (
                    i, cell(disp_title(e)), e["url"], format(e["stars"], ","), delta, lang_col, cell(brief)))
            else:
                lines.append("| %d | [%s](%s) | %s | %s | %s |" % (
                    i, cell(disp_title(e)), e["url"], format(e["stars"], ","), lang_col, cell(brief)))
    lines += ["", "## 详情", ""]
    for i, e in enumerate(entries, 1):
        if is_feed:
            metric = (e["published_at"][:16] or "—").replace("T", " ")
        elif is_zhihu_col:
            metric = "%s 赞 · %s 评论" % (format(_int(e["meta"].get("voteup")), ","),
                                          format(_int(e["meta"].get("comments")), ","))
        elif is_zhihu:
            metric = e["meta"].get("heat") or "-"
        else:
            metric = "%s★" % format(e["stars"], ",")
        lines += ["### %d. %s（%s）" % (i, e.get("title_disp") or e["title"], metric), ""]
        lines.append("- 链接：%s" % e["url"])
        lines.append("- 主题：%s" % ", ".join(e["meta"].get("topics", [])[:8]))
        lines.append("- 最近推送：%s" % (e["published_at"][:10] or "—"))
        lines.append("- 摘要来源：%s | 翻译：%s" % (e["summary_from"], e["lang"]))
        lines.append("- 中文简介：%s" % e["summary_zh"].replace("\n", " "))
        if e["lang"] != "zh-skip":
            lines.append("- 原文简介：%s" % e["summary"].replace("\n", " "))
        lines.append("")
    lines += ["## 成本与运行统计", "",
              "| 项目 | 数值 | 来源 |", "|---|---|---|",
              "| LLM 调用次数 | %d | 计数 |" % stats["llm_calls"],
              "| 输入 tokens | %s | GLM usage（精确） |" % format(stats["prompt_tokens"], ","),
              "| 输出 tokens | %s | GLM usage（精确） |" % format(stats["completion_tokens"], ","),
              "| 合计 tokens | %s | GLM usage（精确） |" % format(stats["total_tokens"], ","),
              "| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |",
              "| GitHub API 调用 | %d 次（限额 60/时，未认证） | 计数 |" % stats["gh_api"]]
    if stats.get("zhihu_api"):
        lines.append("| 知乎 API 调用 | %d 次（无需登录） | 计数 |" % stats["zhihu_api"])
    if stats.get("csdn_api"):
        lines.append("| CSDN API 调用 | %d 次（无需登录） | 计数 |" % stats["csdn_api"])
    if stats.get("rss_api"):
        lines.append("| RSS 抓取 | %d 次 | 计数 |" % stats["rss_api"])
    if stats.get("hn_api"):
        lines.append("| HN API 调用 | %d 次（官方 Algolia） | 计数 |" % stats["hn_api"])
    lines += [
              "| 总耗时（获取→生成） | %.0f 秒 | 计时，统计系统占用时间 |" % elapsed, ""]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", help="按名运行 config/sources.yaml 中的 github 源")
    ap.add_argument("--query", default=DEFAULT_QUERY.format(
        week=date.fromtimestamp(time.time()).strftime("%Y-%m-%d")))
    ap.add_argument("--per-page", type=int, default=10)
    ap.add_argument("--skip-translate", action="store_true")
    args = ap.parse_args()

    label = None
    trending_since = None
    zhihu_cfg = None
    csdn_cfg = None
    rss_cfg = None
    hn_cfg = None
    if args.source:
        entry = load_source_entry(args.source)
        label = args.source
        STATS["source"] = args.source
        stype = entry.get("type")
        if stype == "github" and entry.get("mode") == "trending":
            trending_since = entry.get("since", "monthly")
            args.query = "%s?since=%s" % (TRENDING_URL, trending_since)
        elif stype == "github":
            args.query = entry.get("query") or ""
            args.per_page = int(entry.get("per_page") or 10)
        elif stype == "zhihu":
            zhihu_cfg = entry
            if entry.get("mode") == "column":
                args.query = "zhihu.com 专栏文章流（%s）" % ",".join(entry.get("columns") or [])
            else:
                args.query = "zhihu.com 热榜（AI 关键词过滤）"
        elif stype == "csdn":
            csdn_cfg = entry
            args.query = "csdn.net 搜索（q=%s，tm=%s，近 %s 天）" % (
                entry.get("query"), entry.get("tm", 2), entry.get("days", 3))
        elif stype == "rss":
            rss_cfg = entry
            args.query = "RSS：%s" % entry.get("url", "")
        elif stype == "hn":
            hn_cfg = entry
            args.query = "hn.algolia.com front_page（points 热点排名）"
    args.query = resolve_query(args.query)

    secret = load_secret()
    token = secret.get("GITHUB_TOKEN", "")
    started = time.time()
    if hn_cfg is not None:
        print("[1/5] Hacker News front_page（取 %s 条，按 points 排序）" % hn_cfg.get("limit", 10))
        repos = fetch_hn(int(hn_cfg.get("limit") or 10))
    elif rss_cfg is not None:
        print("[1/5] RSS：%s（最新 %s 条）" % (rss_cfg.get("url"), rss_cfg.get("limit", 10)))
        repos = fetch_rss(rss_cfg.get("url") or "",
                          int(rss_cfg.get("limit") or 10))
    elif csdn_cfg is not None:
        print("[1/5] CSDN 搜索：q=%s tm=%s size=%s days=%s" % (
            csdn_cfg.get("query"), csdn_cfg.get("tm", 2),
            csdn_cfg.get("size", 30), csdn_cfg.get("days", 3)))
        repos = fetch_csdn_search(csdn_cfg.get("query") or "AI",
                                  int(csdn_cfg.get("tm") or 2),
                                  int(csdn_cfg.get("size") or 30),
                                  int(csdn_cfg.get("days") or 3))
    elif zhihu_cfg is not None and zhihu_cfg.get("mode") == "column":
        print("[1/5] 知乎专栏：%s（每专栏 %s 篇，排序=%s）" % (
            ",".join(zhihu_cfg.get("columns") or []),
            zhihu_cfg.get("per_column", 10), zhihu_cfg.get("rank_by", "updated")))
        repos = fetch_zhihu_columns(zhihu_cfg.get("columns") or [],
                                    int(zhihu_cfg.get("per_column") or 10),
                                    zhihu_cfg.get("rank_by", "updated"))
    elif zhihu_cfg is not None:
        print("[1/5] 知乎热榜：limit=%s ai_filter=%s" % (
            zhihu_cfg.get("limit", 30), zhihu_cfg.get("ai_filter", True)))
        repos = fetch_zhihu_hot(int(zhihu_cfg.get("limit") or 30),
                                bool(zhihu_cfg.get("ai_filter", True)),
                                zhihu_cfg.get("keywords") or [])
    elif trending_since:
        print("[1/5] 解析 Trending 页面：since=%s" % trending_since)
        repos = fetch_trending(trending_since)
    else:
        print("[1/5] 搜索：%s" % args.query)
        repos = search_repos(args.query, args.per_page, token)
    print("      命中 %d 个项目" % len(repos))

    entries = []
    for idx, repo in enumerate(repos, 1):
        print("[2/5][3/5] #%d %s" % (idx, repo["full_name"]))
        summary, src_from = summary_cascade(repo, token)
        title_disp = repo["full_name"]
        if args.skip_translate:
            summary_zh, lang = summary, "zh-skip(--skip-translate)"
        elif repo.get("en_article"):
            title_disp, summary_zh, lang = translate_article(repo["full_name"], summary, secret)
        else:
            summary_zh, lang = translate(summary, secret)
        meta = {"language": repo.get("language"),
                "topics": repo.get("topics") or [],
                "period_delta": repo.get("trending_delta", "")}
        meta.update(repo.get("zhihu_meta") or {})
        meta.update(repo.get("rss_meta") or {})
        entries.append({
            "url_norm": repo["html_url"], "title": repo["full_name"],
            "title_disp": title_disp,
            "url": repo["html_url"], "summary": summary, "summary_zh": summary_zh,
            "summary_from": src_from, "lang": lang, "stars": repo["stargazers_count"],
            "published_at": (repo.get("pushed_at") or "")[:19],
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "meta": meta,
        })
        time.sleep(FETCH_INTERVAL)

    print("[4/5] 存库")
    conn = init_db()
    inserted = store(conn, entries)
    elapsed = time.time() - started
    STATS["elapsed_sec"] = round(elapsed)
    conn.execute("INSERT INTO runs(kind,started_at,finished_at,status,stats) "
                 "VALUES('github-top10',?,?, 'ok', ?)",
                 (datetime.fromtimestamp(started).strftime("%Y-%m-%d %H:%M:%S"),
                  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  json.dumps(STATS, ensure_ascii=False)))
    conn.commit()
    conn.close()
    print("      新增 %d 条（其余为已见去重）" % inserted)

    RESULT_DIR.mkdir(exist_ok=True)
    stem = label if label else "github-ai-top10"
    day_dir = RESULT_DIR / date.today().strftime("%Y-%m-%d")   # 按日期归档（用户要求 #23）
    day_dir.mkdir(parents=True, exist_ok=True)
    out = day_dir / ("%s.md" % stem)
    print("[5/5] 生成 %s" % out)
    render_md(entries, args.query, out, STATS, elapsed, label)


if __name__ == "__main__":
    main()
