#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键流水线：采集（全部启用源）→ 发布 wiki → 邮件通知（design.md §1 全链路）。

手工执行或由 cron 调用（tools/schedule.py 安装定时）。各环节失败相互隔离，
汇总报告与日志见 data/logs/pipeline-<日期>.log。

用法：
  python3 tools/run_pipeline.py            # 全链路（今天）
  python3 tools/run_pipeline.py --no-notify   # 跳过邮件通知
"""
import argparse
import json
import re
import sqlite3
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "data" / "logs"
SOURCES = ROOT / "config" / "sources.yaml"

TIMEOUT_COLLECT = 1800   # 单源采集上限（秒）
TIMEOUT_PUBLISH = 600
TIMEOUT_NOTIFY = 300


def sh(cmd, timeout):
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    return p.returncode, (p.stdout + "\n" + p.stderr).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-notify", action="store_true", help="跳过邮件通知")
    args = ap.parse_args()

    day = date.today()
    day_str = day.strftime("%Y-%m-%d")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / ("pipeline-%s.log" % day_str)
    log_f = log_path.open("a", encoding="utf-8")

    def w(msg):
        line = "[%s] %s" % (datetime.now().strftime("%H:%M:%S"), msg)
        print(line)
        log_f.write(line + "\n")
        log_f.flush()

    started = time.time()
    w("=" * 60)
    w("流水线启动：%s" % day_str)

    # ---- 阶段 1：采集（全部启用源） ----
    cfg = yaml.safe_load(SOURCES.read_text(encoding="utf-8")) or {}
    sources = [s["name"] for s in cfg.get("sources") or [] if s.get("enabled", True)]
    w("阶段1 采集：%d 个源 %s" % (len(sources), sources))
    results = []  # (source, ok, file)
    for name in sources:
        try:
            code, out = sh([sys.executable, str(ROOT / "tools" / "gh_ai_top10.py"),
                            "--source", name], TIMEOUT_COLLECT)
        except subprocess.TimeoutExpired:
            code, out = 124, "超时（%ss）" % TIMEOUT_COLLECT
        f = ROOT / "result" / day_str / ("%s.md" % name)
        ok = code == 0 and f.exists()
        results.append((name, ok, f if ok else None))
        w("  %-28s %s%s" % (name, "OK" if ok else "FAIL",
                            "" if ok else " | " + out[-300:].replace("\n", " ")))
    collect_ok = sum(1 for _, ok, _ in results if ok)

    # ---- 阶段 2：发布 wiki（按日期分组） ----
    w("阶段2 发布 wiki")
    published = []
    for name, ok, f in results:
        if not ok:
            continue
        md = f.read_text(encoding="utf-8")
        m = re.match(r"#\s+(.+)", md)
        title = m.group(1).strip() if m else "%s（%s）" % (name, day_str)
        identify = "digest-%s-%s" % (day.strftime("%Y%m%d"), name)
        try:
            code, out = sh([sys.executable, str(ROOT / "tools" / "mindoc_publish.py"),
                            "--file", str(f), "--name", title,
                            "--identify", identify], TIMEOUT_PUBLISH)
        except subprocess.TimeoutExpired:
            code, out = 124, "超时"
        ok_pub = code == 0
        published.append((name, ok_pub))
        w("  %-28s %s%s" % (title[:26], "OK" if ok_pub else "FAIL",
                            "" if ok_pub else " | " + out[-300:].replace("\n", " ")))
    publish_ok = sum(1 for _, ok in published if ok)

    # ---- 阶段 3：邮件通知 ----
    if args.no_notify:
        w("阶段3 邮件通知：跳过（--no-notify）")
        notify_ok = None
    else:
        w("阶段3 邮件通知")
        try:
            code, out = sh([sys.executable, str(ROOT / "tools" / "email_notify.py"),
                            "--digest-day", day_str], TIMEOUT_NOTIFY)
        except subprocess.TimeoutExpired:
            code, out = 124, "超时"
        notify_ok = code == 0
        w("  %s%s" % ("OK" if notify_ok else "FAIL",
                      "" if notify_ok else " | " + out[-300:].replace("\n", " ")))

    # ---- 汇总 ----
    elapsed = time.time() - started
    w("汇总：采集 %d/%d，发布 %d/%d，通知 %s，耗时 %.0fs，日志 %s" % (
        collect_ok, len(sources), publish_ok, len(published),
        ("跳过" if notify_ok is None else ("OK" if notify_ok else "FAIL")),
        elapsed, log_path))
    w("=" * 60)
    record_verify(day_str, collect_ok, len(sources), publish_ok,
                  notify_ok, elapsed, started)
    sys.exit(0 if collect_ok > 0 else 1)


def record_verify(day_str, collect_ok, total, publish_ok, notify_ok, elapsed, started_ts):
    """在 result/<日期>/summary.md 追加一条运行记录（要求 #54：按天归档防膨胀）。

    耗时≈分钟、token≈万（要求 #53 的约数口径）；每运行一次追加一行。
    """
    import sqlite3
    tokens = calls = 0
    try:
        from datetime import datetime as _dt
        started_iso = _dt.fromtimestamp(started_ts).strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(str(ROOT / "data" / "wise.db"))
        # 只统计本次流水线开始之后的采集记录（避免同日多次运行重复计数）
        for (s,) in conn.execute(
                "SELECT stats FROM runs WHERE kind LIKE 'collect-%' "
                "AND finished_at >= ? AND status='ok'", (started_iso,)):
            try:
                d = json.loads(s)
            except ValueError:
                continue
            tokens += d.get("total_tokens") or 0
            calls += d.get("llm_calls") or 0
        conn.close()
    except Exception:
        pass
    day_dir = ROOT / "result" / day_str
    day_dir.mkdir(parents=True, exist_ok=True)
    spath = day_dir / "summary.md"
    hm = time.strftime("%H:%M")
    row = "| %s | 采集 %d/%d · 发布 %d · 通知 %s | ~%d 分钟 | %d 次调用 · ~%.1f 万 tokens |" % (
        hm, collect_ok, total, publish_ok,
        ("跳过" if notify_ok is None else ("OK" if notify_ok else "FAIL")),
        round(elapsed / 60.0), calls, tokens / 10000.0)
    header = ("# 运行记录（%s）\n\n| 时间 | 结果 | 耗时 | LLM 用量 |\n|---|---|---|---|\n" % day_str)
    text = spath.read_text(encoding="utf-8") if spath.exists() else ""
    text = text.rstrip("\n") + "\n" + row + "\n" if text.strip() else header + row + "\n"
    spath.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
