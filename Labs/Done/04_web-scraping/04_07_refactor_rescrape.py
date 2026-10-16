# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import os
from bs4 import BeautifulSoup
import requests

URL = "http://books.toscrape.com/"
CACHE_FILE = "books_page.html"


def fetch_and_cache_page(url, cache_file):
    """Fetches the webpage if the local cache file does not exist.

    Otherwise, loads and returns the content from the cache.
    """
    if not os.path.exists(cache_file):
        print(f"Fetching live page from {url}...")
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) LearningWebScraper/1.0"
            )
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Successfully saved response to local cache: '{cache_file}'\n")
    else:
        print(
            f"Local cache '{cache_file}' found. Loading content locally to"
            " protect the server!\n"
        )

    with open(cache_file, "r", encoding="utf-8") as f:
        return f.read()


def parse_books(html_content):
    """Parses HTML content using BeautifulSoup and extracts book information

    into a list of structured dictionaries.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    book_pods = soup.find_all("article", class_="product_pod")

    books = []
    for book in book_pods:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").get_text()

        star_classes = book.find("p", class_="star-rating")["class"]
        rating = star_classes[1] if len(star_classes) > 1 else "Unknown"

        books.append({"title": title, "price": price, "rating": rating})

    return books


def main():
    """Main execution function to run the scraper workflow."""
    html_content = fetch_and_cache_page(URL, CACHE_FILE)
    books = parse_books(html_content)

    print(f"Found {len(books)} books on the page. Here are the first 5:\n")
    print("=" * 50)
    for book in books[:5]:
        print(f"Title  : {book['title']}")
        print(f"Price  : {book['price']}")
        print(f"Rating : {book['rating']} Stars")
        print("=" * 50)


if __name__ == "__main__":
    main()