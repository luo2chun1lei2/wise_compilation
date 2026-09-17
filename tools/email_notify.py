#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""邮件通知（ADR-0018，tech.md T13）——公司内部信息允许的通道（内网邮件）。

经公司 SMTP 服务器向同事邮箱发送"新文档更新"通知。
凭据（ai/secret.md，均不入 git）：
  EMAIL_SMTP_HOST / EMAIL_SMTP_PORT / EMAIL_SMTP_SSL(true|false)
  EMAIL_SMTP_USER / EMAIL_SMTP_PASS（内网免认证 relay 可留空）
  EMAIL_FROM（发件人地址）
  EMAIL_TO（收件人，逗号分隔）

用法：
  python3 tools/email_notify.py --test
  python3 tools/email_notify.py --notify "标题" "http://url"
  python3 tools/email_notify.py --digest-day 2026-09-16
"""
import argparse
import json
import re
import smtplib
import sqlite3
import sys
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / "ai" / "secret.md"
DB_PATH = ROOT / "data" / "wise.db"

try:
    import markdown as _md_mod
except ImportError:
    _md_mod = None


def load_secret():
    kv = {}
    for line in SECRET_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*([A-Z_]+):\s*(\S.*)", line)
        if m:
            kv[m.group(1)] = m.group(2).strip()
    return kv


def send_mail(sec, subject, md_content):
    host = sec.get("EMAIL_SMTP_HOST", "")
    if not host:
        print("未配置 EMAIL_SMTP_HOST（ai/secret.md）。发件服务器地址可从邮件客户端设置或 IT 获取。")
        sys.exit(2)
    port = int(sec.get("EMAIL_SMTP_PORT") or 25)
    use_ssl = sec.get("EMAIL_SMTP_SSL", "false").lower() == "true"
    user, password = sec.get("EMAIL_SMTP_USER", ""), sec.get("EMAIL_SMTP_PASS", "")
    sender = sec.get("EMAIL_FROM") or user
    to_list = [x.strip() for x in re.split(r"[,;，；]", sec.get("EMAIL_TO", "")) if x.strip()]
    if not (sender and to_list):
        print("未配置 EMAIL_FROM / EMAIL_TO")
        sys.exit(2)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = ", ".join(to_list)
    msg.attach(MIMEText(md_content, "plain", "utf-8"))
    if _md_mod is not None:
        msg.attach(MIMEText(_md_mod.markdown(md_content, extensions=["tables", "fenced_code"]),
                            "html", "utf-8"))

    if use_ssl:
        srv = smtplib.SMTP_SSL(host, port, timeout=30)
    else:
        srv = smtplib.SMTP(host, port, timeout=30)
        try:
            srv.starttls()
        except smtplib.SMTPException:
            pass  # 内网 relay 常无 TLS
    try:
        if user:
            srv.login(user, password or "")
        srv.sendmail(sender, to_list, msg.as_string())
    finally:
        srv.quit()
    return len(to_list)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--notify", nargs=2, metavar=("TITLE", "URL"))
    ap.add_argument("--digest-day", help="汇总 wise.db 中当日 mindoc-publish 记录")
    args = ap.parse_args()

    sec = load_secret()
    base = sec.get("WIKI_URL", "").rstrip("/")
    book = sec.get("WIKI_BOOK_IDENTIFY", "")

    if args.test:
        n = send_mail(sec, "【AI 资讯汇编】通道测试",
                      "**通道测试** ✅\n\n配置成功，后续新文档将发送到此邮箱。\n\n测试链接：[%s](%s)" % (base or "wiki", base))
        print("测试邮件已发送给 %d 个收件人" % n)
    elif args.notify:
        title, url = args.notify
        n = send_mail(sec, "【AI 资讯汇编】新文档：%s" % title,
                      "**新文档**：[%s](%s)\n\n> 内网地址，需公司网络/VPN 打开" % (title, url))
        print("通知已发送给 %d 个收件人" % n)
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
        body = "**%s 更新（%d 篇）**\n\n%s\n\n---\n[当日目录](%s/docs/%s)\n> 内网地址，需公司网络/VPN 打开" % (
            args.digest_day, n, "\n".join(lines), base, book)
        sent = send_mail(sec, "【AI 资讯汇编】%s 更新（%d 篇）" % (args.digest_day, n), body)
        print("已向 %d 个收件人通知 %d 篇新文档" % (sent, n))


if __name__ == "__main__":
    main()
