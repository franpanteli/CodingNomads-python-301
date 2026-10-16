# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/Web_scraping"

print("1. Fetching the Wikipedia page on Web scraping...")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get(URL, headers=headers)
response.raise_for_status()

# Parse the main page with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 2. Extract and filter links
# Wikipedia main content is typically inside 'div#mw-content-text'
content_div = soup.find("div", id="mw-content-text")
links = content_div.find_all("a", href=True) if content_div else soup.find_all("a", href=True)

valid_wiki_links = []
for link in links:
  href = link["href"]

  # Criteria to keep valid article links and filter out navigation/system links:
  # - Must start with '/wiki/'
  # - Must NOT contain colons (which indicate Special:, Talk:, Help:, File:, etc.)
  # - Must NOT be anchor links (e.g., #cite_note)
  if href.startswith("/wiki/") and ":" not in href and "#" not in href:
    full_url = urljoin("https://en.wikipedia.org", href)
    if full_url not in valid_wiki_links:
      valid_wiki_links.append(full_url)

print(f"-> Found {len(valid_wiki_links)} valid filtered article links.")

# 3. Programmatically follow one of the article links
if valid_wiki_links:
  target_url = valid_wiki_links[0]  # Grab the first valid article link
  print(f"\n2. Following link to secondary article: {target_url}")

  sub_response = requests.get(target_url, headers=headers)
  sub_response.raise_for_status()

  sub_soup = BeautifulSoup(sub_response.text, "html.parser")

  # Extract the article title and paragraph texts
  title_element = sub_soup.find("span", class_="mw-page-title-main")
  article_title = title_element.get_text() if title_element else "Wikipedia Article"

  paragraphs = sub_soup.select("div.mw-parser-output > p")
  article_text = "\n".join(
      [p.get_text() for p in paragraphs if p.get_text().strip()]
  )

  # 4. BONUS TASK: Use RegExp to find all numbers in the text
  # This matches integers, decimals, and comma-separated numbers (e.g., 2026, 3.14, 1,000)
  number_pattern = r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b|\b\d+\b"
  found_numbers = re.findall(number_pattern, article_text)

  # 5. Save the text content and extracted numbers to a local text file
  filename = "wikipedia_article_output.txt"
  with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Article Title: {article_title}\n")
    f.write(f"Source URL: {target_url}\n")
    f.write("=" * 60 + "\n\n")
    f.write("ARTICLE TEXT CONTENT:\n")
    f.write(article_text)
    f.write("\n\n" + "=" * 60 + "\n")
    f.write(
        f"BONUS TASK - NUMBERS FOUND IN TEXT ({len(found_numbers)} total):\n"
    )
    f.write(", ".join(found_numbers))

  print(
      f"\nSuccess! Article text and {len(found_numbers)} extracted numbers saved"
      f" to '{filename}'."
  )
else:
  print("No valid Wikipedia article links were found.")
