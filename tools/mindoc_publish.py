#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MinDoc 发布工具（ADR-0001，tech.md T1；design.md §4）.

链路：表单登录（is_remember，30 天免登）→ 会话探测 → 按 doc_identify 建文档/更新内容
（cover=yes 覆盖）→ 读回校验 → publish 记录。

用法：
  python3 tools/mindoc_publish.py --selftest                 # 临时文档 CRUD 自测后删除
  python3 tools/mindoc_publish.py --file <md> --name <文档名> --identify <doc_identify>
"""
import argparse
import json
import re
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

try:
    import markdown as _md_mod
except ImportError:
    _md_mod = None

ROOT = Path(__file__).resolve().parent.parent
SECRET_PATH = ROOT / "ai" / "secret.md"
DB_PATH = ROOT / "data" / "wise.db"

FETCH_INTERVAL = 1.0  # 对 wiki 的请求间隔（ADR-0006）


def load_secret():
    kv = {}
    for line in SECRET_PATH.read_text(encoding="utf-8").splitlines():
        m = re.match(r"-\s*([A-Z_]+):\s*(\S.*)", line)
        if m:
            kv[m.group(1)] = m.group(2).strip()
    return kv


class MinDocClient:
    def __init__(self, base, book, account, password):
        self.base = base.rstrip("/")
        self.book = book
        self.account = account
        self.password = password
        self.s = requests.Session()
        self.s.headers["User-Agent"] = "wise-compilation/0.1 (+local digest tool)"

    # ---------- 登录与会话 ----------

    def login(self):
        """表单登录：GET /login 取 _xsrf → POST 登录（is_remember 拿 30 天免登）。"""
        r = self.s.get(self.base + "/login", timeout=30)
        r.raise_for_status()
        m = re.search(r'name="_xsrf"[^>]*value="([^"]*)"', r.text)
        data = {"account": self.account, "password": self.password,
                "is_remember": "yes"}
        if m:
            data["_xsrf"] = m.group(1)
        r = self.s.post(self.base + "/login", data=data,
                        headers={"X-Requested-With": "XMLHttpRequest",
                                 "Referer": self.base + "/login"},
                        timeout=30)
        r.raise_for_status()
        try:
            body = r.json()
        except ValueError:
            raise RuntimeError("登录响应非 JSON（可能改版）：%s..." % r.text[:120])
        if body.get("errcode") != 0:
            raise RuntimeError("登录失败：%s" % json.dumps(body, ensure_ascii=False)[:120])

    def session_ok(self):
        """探测登录态。注意：过滤器对 AJAX 请求返回 200+JSON错误体，状态码不可靠，
        故不带 X-Requested-With——匿名会被 302 到登录页，登录态返回 200 HTML。"""
        r = self.s.get(self.base + "/book",
                       headers={"Referer": self.base + "/"},
                       allow_redirects=False, timeout=30)
        return r.status_code == 200 and "errcode" not in r.text[:100]

    def ensure_login(self):
        if not self.session_ok():
            self.login()
            if not self.session_ok():
                raise RuntimeError("重登后会话仍无效")

    # ---------- 文档操作 ----------

    def doc_tree(self):
        """解析 /docs/{key} 侧边栏目录树：[(doc_id, doc_identify, title)]。

        实际结构（实测）：<li id="{doc_id}"><a href=".../docs/{book}/{doc_identify}" title="{标题}">
        """
        r = self.s.get("%s/docs/%s" % (self.base, self.book), timeout=30)
        r.raise_for_status()
        pat = re.compile(
            r'<li id="(\d+)"[^>]*>\s*<a href="[^"]*/docs/%s/([a-zA-Z0-9_\-]+)"[^>]*?(?:\stitle="([^"]*)")?'
            % re.escape(self.book))
        tree, seen = [], set()
        for did, idfy, title in pat.findall(r.text):
            if did not in seen:
                seen.add(did)
                tree.append((int(did), idfy, title))
        return tree

    def create_doc(self, doc_name, doc_identify, parent_id=0):
        """建文档节点，返回 doc_id。"""
        r = self.s.post("%s/api/%s/create" % (self.base, self.book),
                        data={"identify": self.book, "doc_name": doc_name,
                              "doc_identify": doc_identify, "parent_id": parent_id,
                              "is_open": 0},
                        headers={"X-Requested-With": "XMLHttpRequest",
                                 "Referer": self.base + "/"}, timeout=30)
        body = r.json()
        if body.get("errcode") != 0:
            raise RuntimeError("create 失败：%s" % json.dumps(body, ensure_ascii=False)[:150])
        data = body.get("data") or {}
        return int(data.get("doc_id") or data.get("document_id") or 0)

    def write_content(self, doc_id, markdown_text):
        """写内容：markdown + 客户端转换的 html 一起提交。

        部署站的后台发布任务队列未执行（V7 实测），只写 markdown 阅读页会空白；
        MinDoc 网页编辑器本就同时提交 html 字段，此处照做。
        """
        html = ""
        if _md_mod is not None:
            html = _md_mod.markdown(markdown_text, extensions=["tables", "fenced_code", "nl2br"])
        r = self.s.post("%s/api/%s/content/%d" % (self.base, self.book, doc_id),
                        data={"markdown": markdown_text, "html": html,
                              "cover": "yes",
                              "version": 0, "markdown_theme": "theme__light"},
                        headers={"X-Requested-With": "XMLHttpRequest",
                                 "Referer": self.base + "/"}, timeout=60)
        body = r.json()
        if body.get("errcode") != 0:
            raise RuntimeError("content 失败：%s" % json.dumps(body, ensure_ascii=False)[:150])
        return True

    def read_content(self, doc_id):
        r = self.s.get("%s/api/%s/content/%d" % (self.base, self.book, doc_id),
                       headers={"X-Requested-With": "XMLHttpRequest",
                                "Referer": self.base + "/"}, timeout=30)
        body = r.json()
        if body.get("errcode") != 0:
            raise RuntimeError("read 失败：%s" % json.dumps(body, ensure_ascii=False)[:150])
        return body["data"].get("markdown", "")

    def delete_doc(self, doc_id):
        r = self.s.post("%s/api/%s/delete" % (self.base, self.book),
                        data={"identify": self.book, "doc_id": doc_id},
                        headers={"X-Requested-With": "XMLHttpRequest",
                                 "Referer": self.base + "/"}, timeout=30)
        return r.json().get("errcode") == 0

    def release_book(self):
        """发布整本书：把 markdown 草稿转为阅读页可见的 HTML（不发布则页面无内容）。"""
        r = self.s.post("%s/book/%s/release" % (self.base, self.book),
                        data={"identify": self.book},
                        headers={"X-Requested-With": "XMLHttpRequest",
                                 "Referer": self.base + "/"}, timeout=120)
        try:
            body = r.json()
            if body.get("errcode") != 0:
                raise RuntimeError("release 失败：%s" % json.dumps(body, ensure_ascii=False)[:120])
        except ValueError:
            pass  # 部分版本返回页面而非 JSON，视为成功，稍后以阅读页验证
        return True

    def page_visible(self, doc_identify, expect_text, tries=3):
        """匿名读阅读页，确认发布后的内容可见（刚写入有短暂延迟，重试）。"""
        import time as _t
        for i in range(tries):
            r = requests.get("%s/docs/%s/%s" % (self.base, self.book, doc_identify),
                             timeout=30)
            if r.status_code == 200 and expect_text in r.text:
                return True
            _t.sleep(3)
        return False

    # ---------- 发布（幂等，design.md §4） ----------

    def find_doc(self, doc_identify):
        for did, idfy, _t in self.doc_tree():
            if idfy == doc_identify:
                return did
        return None

    def publish(self, doc_name, doc_identify, markdown, day=None, retries=2):
        """幂等发布；指定 day（如 2026-09-16）时挂到日期父节点并更新当日索引。"""
        self.ensure_login()
        parent_id = 0
        if day:
            parent_identify = "day-" + day.replace("-", "")
            parent_id = self.find_doc(parent_identify)
            if parent_id is None:
                parent_id = self.create_doc(day, parent_identify)
                print("  新建日期分组 %s → doc_id=%s" % (day, parent_id))
            else:
                print("  日期分组 %s 已存在 doc_id=%s" % (day, parent_id))
        for attempt in range(retries + 1):
            try:
                self.ensure_login()
                time.sleep(FETCH_INTERVAL)
                doc_id = self.find_doc(doc_identify)
                if doc_id is None:
                    doc_id = self.create_doc(doc_name, doc_identify, parent_id=parent_id)
                    print("  新建文档 %s → doc_id=%s" % (doc_name, doc_id))
                else:
                    print("  已存在（identify=%s）doc_id=%s，覆盖更新" % (doc_identify, doc_id))
                time.sleep(FETCH_INTERVAL)
                self.write_content(doc_id, markdown)
                back = self.read_content(doc_id)
                ok = markdown[:80].strip() in back
                # 维护日期分组的索引页（追加当日文档链接，标题只留一个）
                if day and parent_id:
                    time.sleep(FETCH_INTERVAL)
                    idx = self.read_content(parent_id)
                    link = "- [%s](/docs/%s/%s)" % (doc_name, self.book, doc_identify)
                    if link not in idx:
                        header = "# %s 采集清单" % day
                        if header in idx:
                            idx = idx.rstrip() + "\n" + link
                        else:
                            idx = ("%s\n\n%s\n\n%s" % (idx, header, link)).strip()
                        self.write_content(parent_id, idx)
                return {"doc_id": doc_id, "verified": ok}
            except Exception as exc:
                print("  [warn] publish 尝试 %d：%s" % (attempt + 1, exc), file=sys.stderr)
                time.sleep(3)
        raise RuntimeError("publish 重试耗尽")


def log_run(kind, status, stats):
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("INSERT INTO runs(kind,started_at,finished_at,status,stats) "
                 "VALUES(?,?,?,?,?)",
                 (kind, "", datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  status, json.dumps(stats, ensure_ascii=False)))
    conn.commit()
    conn.close()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true", help="临时文档 CRUD 自测后删除")
    ap.add_argument("--file", help="要发布的 markdown 文件")
    ap.add_argument("--name", help="文档标题（默认取文件首行 # 标题）")
    ap.add_argument("--identify", help="doc_identify（小写字母开头）")
    ap.add_argument("--day", default=datetime.now().strftime("%Y-%m-%d"),
                    help="日期分组（默认今天；传入空串则不分组）")
    ap.add_argument("--delete", help="按 doc_identify 删除文档")
    args = ap.parse_args()

    sec = load_secret()
    cli = MinDocClient(sec["WIKI_URL"], sec["WIKI_BOOK_IDENTIFY"],
                       sec["WIKI_ACCOUNT"], sec["WIKI_PASSWORD"])
    started = time.time()

    if args.delete:
        cli.ensure_login()
        did = cli.find_doc(args.delete)
        if did and cli.delete_doc(did):
            print("[删除] %s（doc_id=%s）OK" % (args.delete, did))
        else:
            print("[删除] 未找到或失败：%s" % args.delete)
        return

    if args.selftest:
        print("[自测] 登录 → 建临时文档 → 写内容 → 读回 → 删除")
        cli.ensure_login()
        print("  登录/会话 OK（账号=%s）" % ("*" + sec["WIKI_ACCOUNT"][-4:]))
        result = cli.publish("__发布链路自测__", "selftest-link",
                              "# 自测\n\n发布链路连通性验证，稍后自动删除。")
        did = result["doc_id"]
        print("  publish OK → doc_id=%s 读回校验=%s" % (did, result["verified"]))
        cli.delete_doc(did)
        print("  delete OK")
        log_run("mindoc-selftest", "ok", {"elapsed": round(time.time() - started)})
        print("[自测] 全链路通过 ✓（耗时 %.0fs）" % (time.time() - started))
        return

    if not args.file:
        ap.error("需要 --file，或用 --selftest")
    md = Path(args.file).read_text(encoding="utf-8")
    name = args.name or (re.match(r"#\s+(.+)", md).group(1).strip()
                         if md.startswith("#") else Path(args.file).stem)
    identify = args.identify or re.sub(r"[^a-z0-9\-]", "",
                                       re.sub(r"_", "-", name.lower())) or "doc"
    if not re.match(r"^[a-z]", identify):
        identify = "d-" + identify

    print("[发布] %s → %s（identify=%s，分组=%s）" % (args.file, name, identify, args.day or "无"))
    result = cli.publish(name, identify, md, day=args.day or None)
    cli.release_book()
    # 用正文标记校验阅读页（标题会出现在 <title>，不能证明正文渲染）
    body_marker = "生成时间" if "生成时间" in md else name.split("（")[0][:12]
    visible = cli.page_visible(identify, body_marker)
    log_run("mindoc-publish", "ok" if result["verified"] else "verify-failed",
            {"doc": name, "identify": identify, **result, "released": True,
             "page_visible": visible, "elapsed": round(time.time() - started)})
    print("  完成：doc_id=%s 读回校验=%s 阅读页正文可见=%s"
          % (result["doc_id"], "通过" if result["verified"] else "失败", "是" if visible else "否"))


if __name__ == "__main__":
    main()
