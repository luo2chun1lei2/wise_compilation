#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""企业微信群机器人通知（ADR-0016，tech.md T6）.

向企业微信内部群发送"新文档更新"通知（markdown，含 gr_wiki 链接）。
webhook 地址存 ai/secret.md 的 WECOM_WEBHOOK。

用法：
  python3 tools/wecom_notify.py --test                        # 发送测试消息
  python3 tools/wecom_notify.py --notify "标题" "http://url"   # 发送一条更新通知
  python3 tools/wecom_notify.py --digest-day 2026-09-16        # 汇总当日发布文档发通知
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
MAX_BYTES = 4000  # 官方限制 4096，留余量


def load_secret():
    kv = {}
    for line in SECRET_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*([A-Z_]+):\s*(\S.*)", line)
        if m:
            kv[m.group(1)] = m.group(2).strip()
    return kv


def send_markdown(webhook, content):
    if len(content.encode("utf-8")) > MAX_BYTES:
        content = content.encode("utf-8")[:MAX_BYTES - 20].decode("utf-8", "ignore") + "\n…"
    r = requests.post(webhook, json={"msgtype": "markdown",
                                     "markdown": {"content": content}}, timeout=30)
    body = r.json()
    if body.get("errcode") != 0:
        raise RuntimeError("发送失败：%s" % json.dumps(body, ensure_ascii=False)[:150])
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--notify", nargs=2, metavar=("TITLE", "URL"))
    ap.add_argument("--digest-day", help="汇总 wise.db 中当日 mindoc-publish 记录")
    args = ap.parse_args()

    sec = load_secret()
    hook = sec.get("WECOM_WEBHOOK", "")
    if not hook or hook.startswith("<") or "KEY" in hook.upper() and "qyapi" not in hook:
        print("未配置 WECOM_WEBHOOK（ai/secret.md）。获取方式：企业微信群 → 群设置 → 群机器人 → 添加 → 复制 Webhook 地址。")
        sys.exit(2)

    if args.test:
        send_markdown(hook, "**AI 资讯汇编** 通道测试 ✅\n> 配置成功，后续新文档将推送到本群。")
        print("测试消息已发送")
    elif args.notify:
        title, url = args.notify
        send_markdown(hook, "**AI 资讯汇编 · 新文档**\n> [%s](%s)\n> （内网地址，需在公司网络/VPN 打开）" % (title, url))
        print("通知已发送：%s" % title)
    elif args.digest_day:
        conn = sqlite3.connect(str(DB_PATH))
        rows = conn.execute(
            "SELECT stats FROM runs WHERE kind='mindoc-publish' AND status='ok' "
            "AND finished_at LIKE ? ORDER BY id", (args.digest_day + "%",)).fetchall()
        conn.close()
        lines = ["**AI 资讯汇编 · %s 更新**" % args.digest_day, ""]
        n = 0
        base = sec.get("WIKI_URL", "").rstrip("/")
        book = sec.get("WIKI_BOOK_IDENTIFY", "")
        for (s,) in rows:
            try:
                d = json.loads(s)
            except ValueError:
                continue
            if d.get("identify", "").startswith("day-"):
                continue  # 日期索引页不单独通知
            n += 1
            lines.append("> %d. [%s](%s/docs/%s/%s)" % (n, d["doc"], base, book, d["identify"]))
        if n == 0:
            print("当日无发布记录")
            return
        lines.append("")
        lines.append("[当日目录](%s/docs/%s)" % (base, book))
        send_markdown(hook, "\n".join(lines))
        print("已通知 %d 篇新文档" % n)


if __name__ == "__main__":
    main()
