#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全通路复检脚本（要求 #60）：对项目调查过的所有来源跑 SOP 8 步清单。

对每个站点检查：rel=alternate（RSS 自动发现）、常见 RSS 路径、sitemap、robots.txt
（含 Sitemap 声明）；外网站点走 VPN 代理。输出紧凑矩阵。
"""
import re
import requests
import concurrent.futures as cf

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
PROXY = {"http": "http://127.0.0.1:10077", "https": "http://127.0.0.1:10077"}

SITES = [
    # (名称, 基址, 走代理?)
    ("知乎", "https://www.zhihu.com", False),
    ("CSDN", "https://so.csdn.net", False),
    ("量子位", "https://www.qbitai.com", False),
    ("机器之心", "https://www.jiqizhixin.com", False),
    ("智源社区", "https://hub.baai.ac.cn", False),
    ("InfoQ中国", "https://www.infoq.cn", False),
    ("智谱官网", "https://www.zhipuai.cn", False),
    ("DeepSeek官网", "https://www.deepseek.com", False),
    ("Qwen官网", "https://qwen.ai", False),
    ("OpenAI", "https://openai.com", False),
    ("Anthropic", "https://www.anthropic.com", False),
    ("TechCrunch", "https://techcrunch.com", False),
    ("LatentSpace", "https://www.latent.space", False),
    ("SimonWillison", "https://simonwillison.net", False),
    ("Interconnects", "https://www.interconnects.ai", False),
    ("TLDR-AI", "https://tldr.tech", False),
    ("arXiv", "https://arxiv.org", False),
    ("NVIDIA博客", "https://blogs.nvidia.com", False),
    ("MIT-TR", "https://www.technologyreview.com", False),
    ("TheVerge", "https://www.theverge.com", False),
    ("ArsTechnica", "https://arstechnica.com", False),
    ("Mistral", "https://mistral.ai", True),
    ("MetaAI", "https://ai.meta.com", True),
    ("VentureBeat", "https://venturebeat.com", True),
    ("DeepMind", "https://deepmind.google", True),
    ("GoogleResearch", "https://research.google", True),
    ("blog.google", "https://blog.google", True),
    ("ImportAI", "https://importai.substack.com", True),
]

RSS_PATHS = ["/rss", "/rss.xml", "/feed", "/feed.xml", "/atom.xml", "/news/rss.xml", "/blog/rss.xml"]
SM_PATHS = ["/sitemap.xml", "/sitemap_index.xml"]


def get(url, proxies, timeout=10):
    try:
        return requests.get(url, headers=UA, proxies=proxies, timeout=timeout)
    except Exception:
        return None


def check_site(item):
    name, base, use_proxy = item
    proxies = PROXY if use_proxy else None
    out = {"name": name, "base": base, "proxy": use_proxy,
           "alternate": "", "rss": [], "sitemap": "", "robots": ""}
    r = get(base, proxies, timeout=12)
    if r is not None and r.status_code == 200 and "html" in r.headers.get("content-type", "").lower():
        for m in re.finditer(r'<link[^>]*rel="alternate"[^>]*>', r.text, re.I):
            tag = m.group(0)
            if re.search(r'type="application/(rss|atom)', tag, re.I):
                href = re.search(r'href="([^"]+)"', tag)
                out["alternate"] = (href.group(1) if href else "?")[:70]
                break
    for p in RSS_PATHS:
        r = get(base + p, proxies)
        if r is not None and r.status_code == 200:
            head = (r.text or "")[:200].lstrip().lower()
            if head.startswith("<?xml") or "<rss" in head or "<feed" in head:
                out["rss"].append(p)
    for p in SM_PATHS:
        r = get(base + p, proxies)
        if r is not None and r.status_code == 200:
            head = (r.text or "")[:200].lstrip().lower()
            if head.startswith("<?xml") and ("sitemap" in head or "<urlset" in head):
                out["sitemap"] = p
                break
    r = get(base + "/robots.txt", proxies)
    if r is not None and r.status_code == 200:
        sm = re.findall(r"Sitemap:\s*(\S+)", r.text)
        out["robots"] = ("有Sitemap声明:" + sm[0][:50]) if sm else "有(无Sitemap声明)"
    return out


def main():
    results = []
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for res in ex.map(check_site, SITES):
            results.append(res)
            alt = res["alternate"] or "—"
            rss = ",".join(res["rss"]) or "—"
            sm = res["sitemap"] or "—"
            rb = res["robots"] or "—"
            px = "🪜" if res["proxy"] else " "
            print("%s %-14s alt=%-52s rss=%-22s sm=%-14s robots=%s" % (
                px, res["name"], alt[:52], rss[:22], sm, rb[:40]))


if __name__ == "__main__":
    main()
