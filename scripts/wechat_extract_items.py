#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


INTENT_PATTERNS = [
    ("sell", re.compile(r"^(?:套?出|出掉|出个|出一些|出一[些个]|出|打包出|低价出|便宜出)")),
    ("buy", re.compile(r"^(?:严肃收|求购|求收|蹲一个|蹲|收收|收个|收一张|收|想要)")),
    ("give", re.compile(r"^(?:免费送|送一瓶|送两把|送|附赠)")),
    ("group_buy", re.compile(r"^(?:拼|拼单|有人拼吗|可加)")),
    ("errand", re.compile(r"^(?:求一位同学.*跑腿|帮带进|帮忙跑腿)")),
]

STOP_PREFIXES = [
    "出了",
    "已出",
    "已找到",
    "我要了",
    "行吗",
    "我有",
    "多少",
    "空白的应该",
    "卧槽",
    "看看",
    "是可折叠的是吗",
    "可小刀",
    "价格可议",
    "完全无损",
    "在学勤书院的小餐车",
    "毕业季可以带走跟小猫最美好的回忆",
    "大黄萌萌地看着你",
    "另外附赠徽章一个",
    "娃衣本身和图上一样",
    "但是我不会穿。所以就没拍",
    "111",
    "捞",
    "就是",
    "示意图如下",
    "以上学勤A自提",
    "这个是上面那个",
    "分开也行",
]

TRAILING_PATTERNS = [
    r"[，,。；; ]*价格可议.*$",
    r"[，,。；; ]*可小刀.*$",
    r"[，,。；; ]*学勤[a-zA-Z]?自取.*$",
    r"[，,。；; ]*道扬自取.*$",
    r"[，,。；; ]*下园自取.*$",
    r"[，,。；; ]*有意者.*$",
    r"[，,。；; ]*任意时间.*$",
    r"[，,。；; ]*\d+\s*rmb.*$",
    r"[，,。；; ]*\d+\s*r.*$",
    r"[，,。；; ]*原价.*$",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract item and intent from normalized WeChat CSV.")
    parser.add_argument("--input", required=True, help="Normalized CSV input.")
    parser.add_argument("--output", required=True, help="Structured CSV output.")
    return parser.parse_args()


def detect_intent(content: str) -> str:
    if "免费送" in content:
        return "give"
    if "帮带进" in content or "跑腿" in content:
        return "errand"
    if re.search(r"\d+\s*(?:r|rmb|元|块)", content, flags=re.IGNORECASE):
        if any(key in content for key in ("收", "求", "蹲", "想要")):
            return "buy"
        return "sell"
    for intent, pattern in INTENT_PATTERNS:
        if pattern.search(content):
            return intent
    return "other"


def should_drop(content: str) -> bool:
    stripped = content.strip()
    if not stripped or stripped in {"[图片]", "[聊天记录]"}:
        return True
    for prefix in STOP_PREFIXES:
        if stripped.startswith(prefix):
            return True
    return False


def normalize_item(text: str) -> str:
    item = text.strip()
    if item.startswith("收收纳箱"):
        item = "收纳箱"
    item = re.sub(r"^(?:套?出|出掉|出个|出一些|出一[些个]|出|打包出|低价出|便宜出)", "", item)
    item = re.sub(r"^(?:严肃收|求购|求收|蹲一个|蹲|收收|收个|收一张|收|想要)", "", item)
    item = re.sub(r"^(?:免费送|送一瓶|送两把|送|附赠)", "", item)
    item = re.sub(r"^(?:拼单群|拼单|拼)", "", item)
    item = re.sub(r"^(?:有没有近期要去|有没有还没吃饭的|请问有没有人.*看到一个)", "", item)
    item = re.sub(r"^一位同学下周一帮忙跑腿[:：]?", "", item)
    item = item.lstrip(" ：:，,")
    for pattern in TRAILING_PATTERNS:
        item = re.sub(pattern, "", item, flags=re.IGNORECASE)
    if " " in item:
        item = item.split(" ", 1)[0]
    item = re.split(r"[，,。；;（(]+", item.strip())[0] if item.strip() else ""
    if item == "纳箱":
        item = "收纳箱"
    return item.strip("@")


def main() -> None:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    rows_out: list[list[str]] = []
    with input_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            content = (row.get("content") or "").strip()
            if should_drop(content):
                continue
            intent = detect_intent(content)
            if intent == "other":
                continue
            item = normalize_item(content)
            if not item:
                continue
            rows_out.append(
                [
                    row.get("row_id", ""),
                    row.get("approx_timestamp", ""),
                    row.get("sender", ""),
                    intent,
                    item,
                    content,
                ]
            )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["row_id", "approx_timestamp", "sender", "intent", "item", "content"])
        writer.writerows(rows_out)

    print(f"Extracted rows: {len(rows_out)}")
    print(f"Wrote CSV: {output_path}")


if __name__ == "__main__":
    main()
