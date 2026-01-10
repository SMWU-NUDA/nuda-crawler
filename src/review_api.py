# -*- coding: utf-8 -*-

import json
import csv
import os

response_text = """
"""

response = json.loads(response_text,strict=False)
data = response["data"]

goodsNumber = data[0]["goodsDto"]["goodsNumber"]
option_name = data[0]["goodsDto"]["optionName"]
contents = [review.get("content") for review in data]

file_path = "reviews.csv"
file_exists = os.path.isfile(file_path)

added_count = 0

with open(file_path, mode="a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["product_id", "group_name", "review_content"])

    for content in contents:
        if not content or not content.strip():
            continue
        writer.writerow([
            goodsNumber,
            option_name,
            content.strip()
        ])
        added_count += 1

print(f"이번 실행으로 추가된 리뷰 수: {added_count}")
