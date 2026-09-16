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
from datetime import date, datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / "ai" / "secret.md"
DATA_DIR = ROOT / "data"
RESULT_DIR = ROOT / "result"
DB_PATH = DATA_DIR / "wise.db"

MAX_TRANSLATE_BYTES = 5000   # ADR-0010 翻译上限（UTF-8 字节）
MIN_DESC_BYTES = 80          # 描述过短时从 README 文首补充摘要
HEAD_SUMMARY_BYTES = 1500    # README 文首提取的摘要上限
FETCH_INTERVAL = 1.0         # 对 github.com 的请求间隔（ADR-0006 礼貌抓取）
DEFAULT_QUERY = "topic:artificial-intelligence stars:>500 pushed:>{week}"


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


def gh_headers(token, raw=False):
    h = {"Accept": "application/vnd.github.raw" if raw else "application/vnd.github+json"}
    if token:
        h["Authorization"] = "Bearer " + token
    return h


# ---------- 步骤 1：获取材料 ----------

def search_repos(query, per_page, token):
    url = "https://api.github.com/search/repositories"
    r = requests.get(url, params={"q": query, "sort": "stars", "order": "desc",
                                  "per_page": per_page},
                     headers=gh_headers(token), timeout=30)
    r.raise_for_status()
    return r.json()["items"]


def fetch_readme(full_name, token):
    url = "https://api.github.com/repos/%s/readme" % full_name
    r = requests.get(url, headers=gh_headers(token, raw=True), timeout=30)
    if r.status_code == 404:
        return ""
    r.raise_for_status()
    return r.text


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
    """级联：description → README 文首 → 空串。返回 (summary, source)。"""
    desc = (repo.get("description") or "").strip()
    if len(desc.encode("utf-8")) >= MIN_DESC_BYTES:
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
            out = r.json()["choices"][0]["message"].get("content", "").strip()
            if out:
                return out, "llm"
        except Exception as exc:
            print("  [warn] llm attempt%d: %s" % (attempt, exc), file=sys.stderr)
            time.sleep(3)
    return text, "translate-failed"


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


def render_md(entries, query, out_path):
    lines = [
        "# GitHub AI 热门项目 Top %d" % len(entries), "",
        "- 生成时间：%s" % datetime.now().strftime("%Y-%m-%d %H:%M"),
        "- 数据来源：GitHub Search API（官方接口，按 star 数降序）",
        "- 查询条件：`%s`" % query,
        "- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布", "",
        "| 排名 | 项目 | Stars | 语言 | 中文简介 |", "|---|---|---|---|---|",
    ]
    for i, e in enumerate(entries, 1):
        brief = e["summary_zh"].split("\n")[0][:120]
        lines.append("| %d | [%s](%s) | %s | %s | %s |" % (
            i, e["title"], e["url"], format(e["stars"], ","), e["meta"].get("language") or "-",
            cell(brief)))
    lines += ["", "## 详情", ""]
    for i, e in enumerate(entries, 1):
        lines += ["### %d. %s（%s★）" % (i, e["title"], format(e["stars"], ",")), ""]
        lines.append("- 链接：%s" % e["url"])
        lines.append("- 主题：%s" % ", ".join(e["meta"].get("topics", [])[:8]))
        lines.append("- 最近推送：%s" % e["published_at"][:10])
        lines.append("- 摘要来源：%s | 翻译：%s" % (e["summary_from"], e["lang"]))
        lines.append("- 中文简介：%s" % e["summary_zh"].replace("\n", " "))
        if e["lang"] != "zh-skip":
            lines.append("- 原文简介：%s" % e["summary"].replace("\n", " "))
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--query", default=DEFAULT_QUERY.format(
        week=date.fromtimestamp(time.time()).strftime("%Y-%m-%d")))
    ap.add_argument("--per-page", type=int, default=10)
    ap.add_argument("--skip-translate", action="store_true")
    args = ap.parse_args()

    secret = load_secret()
    token = secret.get("GITHUB_TOKEN", "")
    print("[1/5] 搜索：%s" % args.query)
    repos = search_repos(args.query, args.per_page, token)
    print("      命中 %d 个项目" % len(repos))

    entries = []
    for idx, repo in enumerate(repos, 1):
        print("[2/5][3/5] #%d %s" % (idx, repo["full_name"]))
        summary, src_from = summary_cascade(repo, token)
        if args.skip_translate:
            summary_zh, lang = summary, "zh-skip(--skip-translate)"
        else:
            summary_zh, lang = translate(summary, secret)
        entries.append({
            "url_norm": repo["html_url"], "title": repo["full_name"],
            "url": repo["html_url"], "summary": summary, "summary_zh": summary_zh,
            "summary_from": src_from, "lang": lang, "stars": repo["stargazers_count"],
            "published_at": (repo.get("pushed_at") or "")[:19],
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "meta": {"language": repo.get("language"),
                     "topics": repo.get("topics") or []},
        })
        time.sleep(FETCH_INTERVAL)

    print("[4/5] 存库")
    conn = init_db()
    inserted = store(conn, entries)
    conn.close()
    print("      新增 %d 条（其余为已见去重）" % inserted)

    RESULT_DIR.mkdir(exist_ok=True)
    out = RESULT_DIR / ("github-ai-top10-%s.md" % date.today().strftime("%Y-%m-%d"))
    print("[5/5] 生成 %s" % out)
    render_md(entries, args.query, out)


if __name__ == "__main__":
    main()
