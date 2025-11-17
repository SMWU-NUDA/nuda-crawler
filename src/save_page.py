from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

CATERORY_NO = "100000200040001"
BASE_URL = f"https://www.oliveyoung.co.kr/store/display/getMCategoryList.do?dispCatNo={CATERORY_NO}&pageIdx={{}}"
SAVE_DIR = "html"
TOTAL_PAGE = 16

def scroll_page(driver, times=10):
    for i in range(times):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(1.2)

def save_rendered_html(page_no):
    url = BASE_URL.format(page_no)

    print(f"[INFO] 페이지 {page_no} 접속 중: {url}")

    driver.get(url)
    time.sleep(2.5)

    scroll_page(driver, times=12)

    html = driver.page_source

    os.makedirs(SAVE_DIR, exist_ok=True)
    path = f"{SAVE_DIR}/page_{page_no}.html"

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[INFO] 저장 완료 → {path}")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()

    # 유저 에이전트 넣어서 Cloudflare 우회
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")

    # 브라우저 안 띄우고 실행
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Cloudflare bot detection 우회
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    for page in range(1, TOTAL_PAGE + 1):
        save_rendered_html(page)

    driver.quit()
