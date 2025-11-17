import os
from bs4 import BeautifulSoup
import json
import pandas as pd
import re

def extract_products_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    prd_infos = soup.select("div.prd_info")
    results = []

    for prd in prd_infos:
        try:
            name = prd.select_one(".tx_name").get_text(strip=True)
            brand = prd.select_one(".tx_brand").get_text(strip=True) if prd.select_one(".tx_brand") else None
            link = prd.select_one("a")["href"]
            image = prd.select_one("img")["src"] if prd.select_one("img") else None

            raw_p = prd.select_one(".tx_org .tx_num")
            raw_price = raw_p.get_text(strip=True).replace(",", "") if raw_p else None

            sale_p = prd.select_one(".tx_cur .tx_num")
            sale_price = sale_p.get_text(strip=True).replace(",", "") if sale_p else None

            score_tag = prd.select_one(".review_point .point")
            score = None

            if score_tag:
                style = score_tag.get("style", "")  # 스타일 값이 ""어도 안전하게 처리
                if "width" in style:
                    try:
                        percent_str = style.replace("width:", "").replace("%", "").strip()
                        percent = float(percent_str) if percent_str else None

                        if percent is not None:
                            score = round(percent / 20, 2)
                    except:
                        score = None


            review_tag = prd.select_one(".prd_point_area")
            review_count = None
            if review_tag:
                text = review_tag.get_text(strip=True)  # 10점만점에 5.5점(999+)
                m = re.search(r"\(([\d\+]+)\)", text)   # 괄호 안 숫자만 추출
                review_count = m.group(1) if m else None


            results.append({
                "brand": brand,
                "name": name,
                "link": "https://www.oliveyoung.co.kr" + link,
                "image": image,
                "raw_price": raw_price,
                "sale_price": sale_price,
                "score": score,
                "review_count": review_count,
            })

        except Exception as e:
            print("\n[LOGGING] 파싱 실패:", e)
            print(prd)
            continue


    return results


if __name__ == "__main__":
    base_dir = "html"
    all_products = []

    for i in range(1, 17):   # 페이지 1~16
        file_path = os.path.join(base_dir, f"page_{i}.html")
        
        print(f"[INFO] 페이지 {i} 로컬 HTML 파싱 중…")

        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
            products = extract_products_from_html(html)
            print(f"[INFO] page_{i}: {len(products)} 개 상품 추출")

        all_products.extend(products)

    print(f"\n [DONE] 전체 총 상품 수: {len(all_products)}")

    # 저장
    os.makedirs("data", exist_ok=True)
    pd.DataFrame(all_products).to_csv("data/olive_prd.csv", index=False)
    print("CSV 저장 완료")
