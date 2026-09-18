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
from email.utils import formatdate, make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html import escape as _esc
from pathlib import Path

import yaml

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
            val = re.sub(r"\s+#.*$", "", m.group(2).strip())  # 剥离行内注释
            kv[m.group(1)] = val
    return kv


def fold_details(body_md):
    """把 '## 详情' 下的每个 '### ' 小节折叠为 <details><summary>（用户要求 #42）。

    纯 HTML 无 JS：支持的客户端点击展开；不支持的自动全展开（等价于原样式，零损失）。
    """
    if "## 详情" not in body_md:
        return body_md
    head, detail = body_md.split("## 详情", 1)
    parts = re.split(r"^### ", detail, flags=re.M)
    chunks = []
    for seg in parts[1:]:
        lines = seg.split("\n", 1)
        title = lines[0].strip()
        content = lines[1].strip("\n") if len(lines) > 1 else ""
        chunks.append(
            '<details markdown="1"><summary style="cursor:pointer;"><b>%s</b></summary>\n\n%s\n\n</details>'
            % (_esc(title), content))
    return head + "## 详情\n\n" + "\n\n".join(chunks) + "\n"


def build_mime(subject, text_body, html_body=None):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(subject, "utf-8")
    # 标准头缺失会被反垃圾系统大幅扣分（V11 排查：大 HTML 无 Date/Message-ID 被拦）
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="goldenrivertek.com")
    msg.attach(MIMEText(text_body, "plain", "utf-8"))
    html = html_body
    if html is None and _md_mod is not None:
        html = _md_mod.markdown(text_body, extensions=["tables", "fenced_code"])
    if html:
        msg.attach(MIMEText(html, "html", "utf-8"))
    return msg


def send_mail(sec, subject, md_content, html_body=None):
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

    msg = build_mime(subject, md_content, html_body)
    msg["From"] = sender
    msg["To"] = ", ".join(to_list)

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
        # 全文邮件：内嵌当日各源成果，顶部目录锚点导航（用户要求 #41，wiki 内网外不可达）
        result_dir = ROOT / "result" / args.digest_day
        if not result_dir.exists():
            print("当日无成果目录：%s" % result_dir)
            return
        try:
            order = [s.get("name") for s in (yaml.safe_load(
                (ROOT / "config" / "sources.yaml").read_text(encoding="utf-8")) or {}
            ).get("sources") or []]
        except Exception:
            order = []
        files = sorted(result_dir.glob("*.md"),
                       key=lambda f: (order.index(f.stem) if f.stem in order else 99, f.name))
        if not files:
            print("当日无成果文件")
            return

        base = sec.get("WIKI_URL", "").rstrip("/")
        book = sec.get("WIKI_BOOK_IDENTIFY", "")
        text_parts = ["AI 资讯汇编 · %s 更新（%d 个源）" % (args.digest_day, len(files)),
                      "wiki 当日目录：%s/docs/%s/day-%s（内网）" % (
                          base, book, args.digest_day.replace("-", "")), ""]
        toc_html, sections_html = [], []
        for i, f in enumerate(files, 1):
            md = f.read_text(encoding="utf-8")
            lines = md.splitlines()
            title = next((l[2:].strip() for l in lines if l.startswith("# ")), f.stem)
            body_md = "\n".join(lines[1:]).lstrip("\n")
            n_rows = len(re.findall(r"^### ", body_md, re.M)) or len(
                re.findall(r"^\| \d+ ", body_md, re.M))
            toc_html.append('<li><a href="#sec%d">%s</a>（%d 条）</li>' % (i, _esc(title), n_rows))
            text_parts += ["=" * 46, "%d. %s（%d 条）" % (i, title, n_rows), "=" * 46, body_md]
            body_html = ""
            if _md_mod is not None:
                folded = fold_details(body_md)
                body_html = _md_mod.markdown(
                    folded, extensions=["tables", "fenced_code", "md_in_html"])
                # 邮件客户端吃内联样式：表格加边框
                body_html = body_html.replace(
                    "<table>", '<table border="1" cellpadding="5" cellspacing="0" '
                               'style="border-collapse:collapse;border-color:#bbb;">')
            # 整节折叠（用户要求 #43）：源标题为折叠条，点开才显示表格与详情；条目详情保持二级折叠
            sections_html.append(
                '<details id="sec%d">'
                '<summary style="cursor:pointer;font-size:16px;font-weight:bold;'
                'color:#2a5db0;border-bottom:2px solid #4a90d9;padding:6px 0;">'
                '%d. %s（%d 条）</summary>'
                '<div style="padding-top:8px;">%s</div>'
                '<p style="font-size:12px;"><a href="#toc">↑ 返回目录</a></p>'
                '</details>'
                % (i, i, _esc(title), n_rows, body_html))

        day_url = "%s/docs/%s/day-%s" % (base, book, args.digest_day.replace("-", ""))
        html_body = (
            '<html><body><div style="font-family:-apple-system,\'Microsoft YaHei\',sans-serif;'
            'max-width:960px;margin:0 auto;color:#333;">'
            '<h1 style="color:#2a5db0;">AI 资讯汇编 · %s 更新（%d 个源）</h1>'
            '<p style="color:#888;font-size:13px;">完整 wiki 版本（内网）：<a href="%s">%s</a></p>'
            '<h2 id="toc" style="background:#f0f4fa;padding:8px 12px;">📋 目录（点击跳转；各节点击标题展开）</h2>'
            '<ol style="line-height:1.9;">%s</ol><hr/>%s'
            '</div></body></html>'
        ) % (args.digest_day, len(files), day_url, day_url,
             "".join(toc_html), "".join(sections_html))
        text_body = "\n\n".join(text_parts)
        sent = send_mail(sec, "【AI 资讯汇编】%s 更新（%d 个源）" % (args.digest_day, len(files)),
                          text_body, html_body=html_body)
        print("已向 %d 个收件人发送全文汇总邮件：%d 个源，HTML %.0fKB"
              % (sent, len(files), len(html_body) / 1024.0))


if __name__ == "__main__":
    main()
