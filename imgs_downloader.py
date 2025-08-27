from UI import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
import re
import gzip

def get_images_url(page_url):
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(page_url)

    # Wait for the page to fully load (here using 10 seconds for demo)
    start_time = time.time()
    while time.time() - start_time < 10:
        print_centered("Loading...")  # display loading
        clear_screen()

    # Get the total number of pages
    try:
        span = driver.find_element("css selector", 'input[name="pageNumber"]').find_element("xpath", "following-sibling::*[1]")
        total_pages = int(span.text.replace("/", "").strip())
        print_centered(f"Total pages: {total_pages}")
    except Exception as e:
        print_centered("Unable to find total pages! Connection problem")
        exit()

    # Get performance logs like JS performance.getEntriesByType("resource")
    logs = driver.get_log("performance")
    resources = []
    for entry in logs:
        msg = entry["message"]
        if "Network.responseReceived" in msg and any(ext in msg for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".svgz"]):
            match = re.search(r'"url":"([^"]+)"', msg)
            if match:
                resources.append(match.group(1))

    pattern = re.compile(r'/p\d+\.(jpg|jpeg|png|gif|webp|svg|svgz)(\?.*)?$', re.IGNORECASE)
    images_urls = [res for res in resources if pattern.search(res)]
    url = images_urls[1] if len(images_urls) > 1 else None
    driver.quit()
    return url, total_pages

def download_and_save(page_num, base_url, img_path):
    url = base_url.format(page_num)
    res = requests.get(url)
    if res.status_code == 200:
        raw = res.content
        filename_svg = os.path.join(img_path, f"p{page_num}.svg")
        try:
            svg_data = gzip.decompress(raw)
            with open(filename_svg, "wb") as f:
                f.write(svg_data)
        except Exception:
            with open(filename_svg, "wb") as f:
                f.write(raw)
        return filename_svg
    else:
        print_centered(f"! Page {page_num} not found (status {res.status_code})")
        return None

def imgs_downloader():
    print("\n\n")
    page_url = input_clignotant("Enter the book URL: ")
    url, total_pages = get_images_url(page_url)

    if url:
        base_url = re.sub(r"p\d+\.(?:jpg|jpeg|png|gif|webp|svgz|svg)", "p{}.svgz", url)
    else:
        print(base_url)
        print_centered("Base URL not found! Connection problem")
        exit()

    img_dir = "imgs"
    current_dir = os.getcwd()
    img_path = os.path.join(current_dir, img_dir)
    os.makedirs(img_path, exist_ok=True)

    for i in range(1, total_pages + 1):
        download_and_save(i, base_url, img_path)
        print_download_progress(i, total_pages)
        time.sleep(0.05)
    return total_pages
