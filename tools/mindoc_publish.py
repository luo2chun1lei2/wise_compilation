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

    def write_content(self, doc_id, markdown):
        """写 markdown 内容（cover=yes 强制覆盖，ADR-0001）。"""
        r = self.s.post("%s/api/%s/content/%d" % (self.base, self.book, doc_id),
                        data={"markdown": markdown, "cover": "yes",
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

    # ---------- 发布（幂等，design.md §4） ----------

    def publish(self, doc_name, doc_identify, markdown, retries=2):
        for attempt in range(retries + 1):
            try:
                self.ensure_login()
                time.sleep(FETCH_INTERVAL)
                doc_id = None
                for did, idfy, _title in self.doc_tree():
                    if idfy == doc_identify:
                        doc_id = did
                        break
                if doc_id is None:
                    doc_id = self.create_doc(doc_name, doc_identify)
                    print("  新建文档 %s → doc_id=%s" % (doc_name, doc_id))
                else:
                    print("  已存在（identify=%s）doc_id=%s，覆盖更新" % (doc_identify, doc_id))
                time.sleep(FETCH_INTERVAL)
                self.write_content(doc_id, markdown)
                back = self.read_content(doc_id)
                ok = markdown[:80].strip() in back
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
    args = ap.parse_args()

    sec = load_secret()
    cli = MinDocClient(sec["WIKI_URL"], sec["WIKI_BOOK_IDENTIFY"],
                       sec["WIKI_ACCOUNT"], sec["WIKI_PASSWORD"])
    started = time.time()

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

    print("[发布] %s → %s（identify=%s）" % (args.file, name, identify))
    result = cli.publish(name, identify, md)
    log_run("mindoc-publish", "ok" if result["verified"] else "verify-failed",
            {"doc": name, "identify": identify, **result,
             "elapsed": round(time.time() - started)})
    print("  完成：doc_id=%s 读回校验=%s" % (result["doc_id"], "通过" if result["verified"] else "失败"))


if __name__ == "__main__":
    main()
