#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WxPusher 微信通知（ADR-0017，tech.md T6 修订）.

通过 WxPusher 主题（Topic）向订阅同事的微信推送"新文档更新"通知。
同事侧只需：扫码关注 WxPusher 公众号 → 订阅本应用主题（一次性）。
凭据：ai/secret.md 的 WXPUSHER_APP_TOKEN / WXPUSHER_TOPIC_ID。

用法：
  python3 tools/wxpusher_notify.py --test                        # 发送测试消息
  python3 tools/wxpusher_notify.py --notify "标题" "http://url"   # 单条更新通知
  python3 tools/wxpusher_notify.py --digest-day 2026-09-16        # 汇总当日发布文档
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / "ai" / "secret.md"
DB_PATH = ROOT / "data" / "wise.db"
API = "https://wxpusher.zjiecode.com/api/send/message"
# contentType: 1=文本 2=HTML 3=markdown（WxPusher 文档）
CONTENT_TYPE_MARKDOWN = 3


def load_secret():
    kv = {}
    for line in SECRET_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*([A-Z_]+):\s*(\S.*)", line)
        if m:
            kv[m.group(1)] = m.group(2).strip()
    return kv


def send(secret, content, title="AI 资讯汇编", url=None):
    payload = {
        "appToken": secret["WXPUSHER_APP_TOKEN"],
        "content": content,
        "summary": title[:100],            # 微信消息列表里显示的摘要
        "contentType": CONTENT_TYPE_MARKDOWN,
        "topicIds": [int(secret["WXPUSHER_TOPIC_ID"])],
    }
    if url:
        payload["urlParam"] = url          # 消息点开跳转
    r = requests.post(API, json=payload, timeout=30)
    body = r.json()
    if not body.get("success") or body.get("code") != 1000:
        raise RuntimeError("发送失败：%s" % json.dumps(body, ensure_ascii=False)[:200])
    return body.get("data")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--notify", nargs=2, metavar=("TITLE", "URL"))
    ap.add_argument("--digest-day", help="汇总 wise.db 中当日 mindoc-publish 记录")
    args = ap.parse_args()

    sec = load_secret()
    if not sec.get("WXPUSHER_APP_TOKEN") or not sec.get("WXPUSHER_TOPIC_ID"):
        print("未配置 WXPUSHER_APP_TOKEN / WXPUSHER_TOPIC_ID（ai/secret.md）。\n"
              "获取：wxpusher.zjiecode.com 微信扫码登录 → 创建应用（appToken）→ 创建主题（topicId）。")
        sys.exit(2)

    base = sec.get("WIKI_URL", "").rstrip("/")
    book = sec.get("WIKI_BOOK_IDENTIFY", "")

    if args.test:
        n = send(sec, "**通道测试** ✅\n\n配置成功，后续新文档将推送到微信。", "通道测试")
        print("测试消息已发送（resp:%s）" % n)
    elif args.notify:
        title, url = args.notify
        send(sec, "**新文档**：[%s](%s)\n\n> 内网地址，需公司网络/VPN 打开" % (title, url), title, url)
        print("通知已发送：%s" % title)
    elif args.digest_day:
        conn = sqlite3.connect(str(DB_PATH))
        rows = conn.execute(
            "SELECT stats FROM runs WHERE kind='mindoc-publish' AND status='ok' "
            "AND finished_at LIKE ? ORDER BY id", (args.digest_day + "%",)).fetchall()
        conn.close()
        lines, n = [], 0
        for (s,) in rows:
            try:
                d = json.loads(s)
            except ValueError:
                continue
            if d.get("identify", "").startswith("day-"):
                continue
            n += 1
            lines.append("%d. [%s](%s/docs/%s/%s)" % (n, d["doc"], base, book, d["identify"]))
        if n == 0:
            print("当日无发布记录")
            return
        content = "**%s 更新（%d 篇）**\n\n%s\n\n---\n[当日目录](%s/docs/%s)\n> 内网地址，需公司网络/VPN 打开" % (
            args.digest_day, n, "\n".join(lines), base, book)
        send(sec, content, "AI 资讯汇编 %s 更新" % args.digest_day, "%s/docs/%s" % (base, book))
        print("已通知 %d 篇新文档" % n)


if __name__ == "__main__":
    main()
