# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import os
from bs4 import BeautifulSoup
import requests

URL = "http://books.toscrape.com/"
CACHE_FILE = "books_page.html"

# --- STEP 1: Be respectful and limit calls by caching the response ---
if not os.path.exists(CACHE_FILE):
  print(f"Fetching live page from {URL}...")
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) LearningWebScraper/1.0"
      )
  }
  response = requests.get(URL, headers=headers)
  response.raise_for_status()

  # Save response to a local file
  with open(CACHE_FILE, "w", encoding="utf-8") as f:
    f.write(response.text)
  print(f"Successfully saved response to local cache file: '{CACHE_FILE}'\n")
else:
  print(
      f"Local cache file '{CACHE_FILE}' found. Loading content locally to"
      " protect the server!\n"
  )

# --- STEP 2: Parse the content from the local file ---
with open(CACHE_FILE, "r", encoding="utf-8") as f:
  html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# --- STEP 3: Extract information of interest ---
# Find all book containers on the page
book_pods = soup.find_all("article", class_="product_pod")

print(f"Found {len(book_pods)} books on the page. Here are the first 5:\n")
print("=" * 50)

for book in book_pods[:5]:
  # Extract title (stored in the 'title' attribute of the nested <a> tag)
  title = book.h3.a["title"]

  # Extract price
  price = book.find("p", class_="price_color").get_text()

  # Extract star rating (e.g., class="star-rating Three")
  star_classes = book.find("p", class_="star-rating")["class"]
  rating = star_classes[1] if len(star_classes) > 1 else "Unknown"

  print(f"Title  : {title}")
  print(f"Price  : {price}")
  print(f"Rating : {rating} Stars")
  print("=" * 50)