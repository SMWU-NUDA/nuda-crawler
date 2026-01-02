from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time
import os
import csv
import re
import random
from urllib.parse import urljoin

CATERORY_NO = "100000200040001"
BASE_URL = f"https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={CATERORY_NO}&pageIdx={{}}"
TOTAL_PAGE = 14
OUT_CSV = "oliveyoung_products.csv"

DEBUG = True                 
DETAIL_ENRICH = True         
DETAIL_LIMIT = None          


def get_chromedriver_path():
    driver_path = ChromeDriverManager().install()
    base_dir = os.path.dirname(driver_path)
    base_name = os.path.basename(driver_path)

    if base_name.startswith("THIRD_PARTY_NOTICES"):
        for fn in os.listdir(base_dir):
            if fn == "chromedriver":
                driver_path = os.path.join(base_dir, fn)
                break

    try:
        os.chmod(driver_path, 0o755)
    except Exception:
        pass

    return driver_path


def human_sleep(base=1.2, jitter=0.8):
    time.sleep(base + random.random() * jitter)


def is_wait_page(driver):
    t = (driver.title or "").strip()
    if "잠시만 기다리십시오" in t:
        return True
    html = (driver.page_source or "")
    if "잠시만 기다리십시오" in html:
        return True
    return False


def scroll_page(driver, times=12):
    body = driver.find_element(By.TAG_NAME, "body")
    for _ in range(times):
        body.send_keys(Keys.END)
        time.sleep(1.0)


def safe_text(el):
    try:
        return el.text.strip()
    except Exception:
        return ""


def first_match_text(root, selectors):
    for css in selectors:
        try:
            el = root.find_element(By.CSS_SELECTOR, css)
            txt = safe_text(el)
            if txt:
                return txt
        except Exception:
            pass
    return ""


def first_match_attr(root, selectors, attr):
    for css in selectors:
        try:
            el = root.find_element(By.CSS_SELECTOR, css)
            val = el.get_attribute(attr)
            if val:
                return val.strip()
        except Exception:
            pass
    return ""


# =========================
# List page parsing
# =========================
def extract_products_from_list_page(driver, debug=False):
    card_selectors = [
        "ul.cate_prd_list > li",
        "ul.prod-list > li",
        "li.prd_info",
    ]

    cards = []
    for sel in card_selectors:
        cards = driver.find_elements(By.CSS_SELECTOR, sel)
        if cards:
            break

    items = []
    for idx, card in enumerate(cards):
        try:
            name = first_match_text(card, ["p.prd_name", "p.tx_name", "a .tx_name"])
            brand = first_match_text(card, ["span.tx_brand", "p.tx_brand", ".brand"])

            if debug and idx == 0:
                print("\n===== DEBUG LIST CARD (LI) TEXT =====")
                print(card.get_attribute("innerText"))
                print("===== END LIST CARD =====\n")

            cur_price = first_match_text(card, ["span.tx_cur", "span.tx_cur > span", ".tx_cur"])
            org_price = first_match_text(card, ["span.tx_org", "span.tx_org > span", ".tx_org"])
            sale_price = first_match_text(card, ["span.tx_num", "span.tx_sale", ".tx_num"])

            link = first_match_attr(card, ["a.prd_thumb", "a[href*='goodsNo']", "a"], "href")
            if link and link.startswith("/"):
                link = urljoin("https://www.oliveyoung.co.kr", link)

            img = first_match_attr(card, ["a.prd_thumb img", "img"], "src")

            if not name and not link:
                continue

            goods_no = ""
            if link:
                m = re.search(r"goodsNo=([A-Z0-9]+)", link)
                if m:
                    goods_no = m.group(1)

            items.append({
                "goods_no": goods_no,
                "name": name,
                "brand": brand,
                "cur_price": cur_price,
                "org_price": org_price,
                "sale_price": sale_price,
                "rating": "",
                "review_cnt": "",
                "link": link,
                "img": img,
            })

        except StaleElementReferenceException:
            continue

    return items


def extract_rating_review_from_detail(driver, url, goods_no="", debug=False, retries=5):
    for attempt in range(1, retries + 1):
        driver.get(url)
        human_sleep(0.8, 0.6)

        if is_wait_page(driver):
            wait_s = min(30, 6 * attempt)  # 6,12,18,24,30
            if debug:
                print("\n===== DEBUG BLOCKED (WAIT PAGE) =====")
                print("goodsNo:", goods_no)
                print("attempt:", attempt, "/", retries)
                print("title:", driver.title)
                print("sleep:", wait_s, "sec")
                print("url:", url)
                print("===== END =====\n")
            time.sleep(wait_s)
            continue

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='ReviewArea_review-area']"))
            )
        except TimeoutException:
            if debug:
                print("\n===== DEBUG DETAIL TIMEOUT =====")
                print("goodsNo:", goods_no)
                print("attempt:", attempt, "/", retries)
                print("title:", driver.title)
                print("url:", url)
                print("===== END =====\n")
            time.sleep(2 + attempt)
            continue

        rating, review_cnt = driver.execute_script(
            """
            const area = document.querySelector("div[class*='ReviewArea_review-area']");
            if(!area) return ["",""];

            const ratingEl = area.querySelector("span.rating");
            const cntEl = area.querySelector("div[class*='ReviewArea_review-count'] button span");

            const rating = ratingEl ? (ratingEl.textContent || ratingEl.innerText || "").trim() : "";
            const cnt = cntEl ? (cntEl.textContent || cntEl.innerText || "").trim() : "";

            return [rating, cnt];
            """
        )

        rating = (rating or "").strip().replace('"', "")
        review_cnt = (review_cnt or "").strip()

        m = re.search(r"(\d\.\d)", rating)
        if m:
            rating = m.group(1)

        if debug:
            print("\n===== DEBUG DETAIL REVIEW =====")
            print("goodsNo:", goods_no)
            print("attempt:", attempt, "/", retries)
            print("rating:", rating)
            print("review_cnt:", review_cnt)
            print("url:", url)
            print("===== END =====\n")

        return rating, review_cnt

    return "", ""


def crawl_all_pages_to_csv(driver, debug=False, enrich_detail=True, detail_limit=None):
    all_items = []
    seen = set()

    for page_no in range(1, TOTAL_PAGE + 1):
        url = BASE_URL.format(page_no)
        print(f"[INFO] 페이지 {page_no} 접속 중: {url}")

        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(1.2)

        scroll_page(driver, times=12)
        time.sleep(0.6)

        items = extract_products_from_list_page(driver, debug=debug)
        print(f"[INFO] 페이지 {page_no} 리스트 수집: {len(items)}")

        for it in items:
            key = it.get("link") or it.get("name")
            if key and key not in seen:
                seen.add(key)
                all_items.append(it)

    print(f"[INFO] 리스트 총 수집: {len(all_items)}")

    if enrich_detail:
        print("[INFO] 상세페이지에서 rating/review 채우는 중...")
        print("[DEBUG] enrich_detail =", enrich_detail)
        print("[DEBUG] detail_limit =", detail_limit)

        target = all_items if detail_limit is None else all_items[:detail_limit]

        for i, it in enumerate(target, 1):
            link = it.get("link")
            if not link:
                continue

            human_sleep(1.2, 1.0)

            rating, review_cnt = extract_rating_review_from_detail(
                driver, link, goods_no=it.get("goods_no", ""), debug=debug, retries=5
            )
            it["rating"] = rating
            it["review_cnt"] = review_cnt

            if i % 10 == 0:
                time.sleep(4)

            if i % 20 == 0:
                print(f"[INFO] 상세 진행: {i}/{len(target)}")

    fieldnames = [
        "goods_no", "name", "brand", "cur_price", "org_price", "sale_price",
        "rating", "review_cnt", "link", "img"
    ]

    with open(OUT_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_items)

    print(f"[INFO] CSV 저장 완료 → {OUT_CSV} (총 {len(all_items)}개)")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )

    options.add_argument("--headless=new")

    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(get_chromedriver_path()),
        options=options
    )

    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    crawl_all_pages_to_csv(
        driver,
        debug=DEBUG,
        enrich_detail=DETAIL_ENRICH,
        detail_limit=DETAIL_LIMIT
    )

    driver.quit()
