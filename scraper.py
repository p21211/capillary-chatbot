
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

BASE_URL = "https://docs.capillarytech.com/"
SAVE_DIR = "data/docs_raw/"

def scrape_docs():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    print(f"🔍 Connecting to {BASE_URL} ...")
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)

    total_links = len(links)
    print(f"🔗 Found {total_links} links on the homepage.")
    visited = set()
    success_count = 0
    failed_count = 0

    for link in tqdm(links, desc="📄 Scraping progress"):
        href = link["href"]
        full_url = urljoin(BASE_URL, href)

        if full_url in visited or not full_url.startswith(BASE_URL) or "#" in href:
            continue

        try:
            page = requests.get(full_url, timeout=10)
            if page.status_code == 200:
                page_soup = BeautifulSoup(page.text, "html.parser")
                text = page_soup.get_text(separator="\n", strip=True)
                if not text.strip():
                    continue
                filename = href.strip("/").replace("/", "_") or "index"
                filepath = os.path.join(SAVE_DIR, f"{filename}.txt")

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"✅ Saved: {filepath}")
                success_count += 1
                visited.add(full_url)
            else:
                print(f"❌ Skipped (status {page.status_code}): {full_url}")
                failed_count += 1
        except Exception as e:
            print(f"❌ Error fetching {full_url} — {str(e)}")
            failed_count += 1

    print("\n📝 Scraping Summary:")
    print(f"✅ Pages saved: {success_count}")
    print(f"❌ Pages failed/skipped: {failed_count}")
    print(f"📂 Files stored in: {SAVE_DIR}")

if __name__ == "__main__":
    scrape_docs()
