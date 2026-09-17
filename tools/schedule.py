#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""定时任务管理（ADR-0006：cron 触发一次性命令，无常驻服务）。

管理 crontab 中属于本项目的托管块（BEGIN/END 标记之间），可重复执行、互不影响其他条目。

用法：
  python3 tools/schedule.py --check                           # 检查 crontab/cron 服务可用性
  python3 tools/schedule.py --install [--cron '30 8 * * *']   # 安装/更新定时（默认每天 08:30）
  python3 tools/schedule.py --remove                          # 移除托管条目
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNNER = ROOT / "tools" / "run_pipeline.py"
BEGIN = "# wise-compilation:begin"
END = "# wise-compilation:end"


def crontab_available():
    return shutil.which("crontab") is not None


def cron_daemon_running():
    for name in ("cron", "crond"):
        try:
            if subprocess.run(["pgrep", "-x", name], capture_output=True).returncode == 0:
                return True
        except FileNotFoundError:
            pass
    return False


def read_crontab():
    p = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def write_crontab(content):
    p = subprocess.run(["crontab", "-"], input=content, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("写入 crontab 失败：%s" % p.stderr.strip()[:200])


def managed_block(text):
    m = re.search(re.escape(BEGIN) + r".*?" + re.escape(END), text, re.S)
    return m.group(0) if m else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--remove", action="store_true")
    ap.add_argument("--cron", default="30 8 * * *", help="cron 表达式（默认每天 08:30）")
    args = ap.parse_args()

    if not (args.check or args.install or args.remove):
        ap.error("需要 --check / --install / --remove 之一")

    if not crontab_available():
        print("❌ 系统无 crontab 命令（cron 不可用），需改用 systemd timer 等方式")
        sys.exit(2)

    current = read_crontab()
    old = managed_block(current)

    if args.check:
        print("crontab 命令：可用")
        print("cron 服务：%s" % ("运行中" if cron_daemon_running()
                                else "未检测到（cron 可能未启动，定时不会生效！）"))
        print("当前托管条目：\n%s" % (old if old else "（未安装）"))
        return

    rest = current.replace(old, "").rstrip("\n") if old else current.rstrip("\n")

    if args.remove:
        write_crontab((rest + "\n") if rest else "")
        print("已移除托管条目")
        return

    if not cron_daemon_running():
        print("⚠️  警告：cron 服务未检测到，条目已写入但不会执行（先启动 cron：sudo service cron start）")
    entry = "%s %s %s >> %s 2>&1" % (
        args.cron, sys.executable, RUNNER, ROOT / "data" / "logs" / "cron.log")
    block = "%s\n# wise_compilation 定时采集发布（tools/schedule.py 管理）\n%s\n%s" % (
        BEGIN, entry, END)
    new = (rest + "\n\n" if rest else "") + block + "\n"
    write_crontab(new)
    print("已安装定时任务：")
    print("  %s" % entry)
    print("日志：%s" % (ROOT / "data" / "logs" / "cron.log"))
    print("变更时间用 --cron '<表达式>' 重新安装；移除用 --remove")


if __name__ == "__main__":
    main()
