#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性迁移（ADR-0022）：旧版「榜单宽表格 + ## 详情」双段格式 → 卡片式条目块。

用途：把布局切换当日已生成的 result/<date>/*.md 就地转为新格式，便于当日重发布；
次日起流水线直接产出新格式，本脚本仅作历史批次迁移工具保留。

用法：python3 tools/reformat_cards.py result/2026-09-21 [--diff 预览不改写]
"""
import argparse
import re
from pathlib import Path


def link_text(t):
    return t.replace("[", "［").replace("]", "］").replace("\n", " ")


def strip_table(head):
    """删除头部信息后的榜单表格（连续的 '| ' 行及其后空行）。"""
    out, in_table = [], False
    for line in head.split("\n"):
        if line.lstrip().startswith("|"):
            in_table = True
            continue
        if in_table and not line.strip():
            continue
        in_table = False
        out.append(line)
    return "\n".join(out).rstrip("\n") + "\n\n"


def table_extras(head):
    """回收旧榜单表格列里、详情段没有的属性：url → {'column':…, 'lang':…}。"""
    extras = {}
    for row in head.split("\n"):
        if not row.startswith("| ") or "---" in row:
            continue
        m = re.match(r"^\| \d+ \| \[.*?\]\(([^)]+)\) \| (.*)$", row.rstrip())
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        info = {}
        if (len(cells) >= 3 and not re.match(r"^[\d,]+$", cells[0])
                and not re.match(r"^\d{4}-\d{2}-\d{2}", cells[0])):  # 专栏/作者列（非数字非日期）
            info["column"] = cells[0]
        lang = next((c for c in cells[1:] if re.match(r"^[A-Za-z0-9+#. -]+$", c)
                     and not re.match(r"^[\d,]+$", c) and "★" not in c and c != "-"), None)
        if lang:
            info["lang"] = lang
        if info:
            extras[m.group(1)] = info
    return extras


def reformat(md):
    """返回 (新文本, 条目数)；非旧格式（无 ## 详情）原样返回 0。"""
    if "## 详情" not in md:
        return md, 0
    head, detail = md.split("## 详情", 1)
    stats = ""
    if "## 成本与运行统计" in detail:
        detail, after = detail.split("## 成本与运行统计", 1)
        stats = "## 成本与运行统计" + after
    extras = table_extras(head)
    blocks = []
    for seg in re.split(r"^### ", detail, flags=re.M)[1:]:
        lines = seg.rstrip("\n").split("\n")
        m = re.match(r"^(\d+)\.\s+(.*)（(.*)）\s*$", lines[0].strip())
        if not m:
            continue
        num, title, metric = m.group(1), link_text(m.group(2)), m.group(3)
        url, attrs, keep = "", [], []
        for line in lines[1:]:
            line = line.strip()
            if not line or line in ("- 主题：", "- 原文简介："):
                continue  # 空行 / 旧版空主题 / 空原文，丢弃
            if line.startswith("- 链接："):
                url = line[len("- 链接："):].strip()
            elif line.startswith("- 主题："):
                attrs.append(line[2:])
            elif line.startswith("- 最近推送："):
                if not re.match(r"^\d{4}-\d{2}-\d{2}", metric):  # feed 类日期已在标题行
                    attrs.append("推送：" + line[len("- 最近推送："):].strip())
            elif line.startswith("- 摘要来源："):
                attrs.append(line[2:].replace("摘要来源：", "摘要：").replace(" | ", " · "))
            else:
                keep.append(line)  # 中文简介 / 原文简介
        if not url:
            continue
        if re.match(r"^\d{4}-\d{2}-\d{2}", metric):  # feed 类指标统一加「发布」前缀
            metric = "发布 " + metric
        extra = extras.get(url) or {}
        if extra.get("lang"):
            metric = "%s · %s" % (metric, extra["lang"])
        if extra.get("column"):
            attrs.insert(0, "来源：%s" % extra["column"])
        block = ["### %s. [%s](%s)（%s）" % (num, title, url, metric), ""]
        block += keep
        if attrs:
            block.append("- %s" % " · ".join(attrs))
        blocks.append("\n".join(block))
    if not blocks:
        return md, 0
    return strip_table(head) + "\n\n".join(blocks) + "\n\n" + stats.lstrip("\n"), len(blocks)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dir", help="result 日期目录，如 result/2026-09-21")
    ap.add_argument("--diff", action="store_true", help="只打印转换结果，不写回")
    args = ap.parse_args()
    d = Path(args.dir)
    changed = 0
    for f in sorted(d.glob("*.md")):
        if f.name == "summary.md":
            continue
        md = f.read_text(encoding="utf-8")
        new, n = reformat(md)
        if n == 0:
            print("  跳过（非旧格式）：%s" % f.name)
            continue
        changed += 1
        if args.diff:
            print("=" * 60, f.name, "（%d 条）" % n, sep="\n")
            print(new)
        else:
            f.write_text(new, encoding="utf-8")
            print("  已转换 %d 条：%s" % (n, f.name))
    print("%s %d 个文件" % ("预览" if args.diff else "完成", changed))


if __name__ == "__main__":
    main()
