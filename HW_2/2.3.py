import requests
import re

def fetch_html(url):
    response = requests.get(url)
    return response.text


def extract_quotes_and_authors(html):
    quotes = re.findall(r'<span class="text" itemprop="text">“(.*?)”</span>', html)
    authors = re.findall(r'<small class="author" itemprop="author">(.*?)</small>', html)
    return list(zip(quotes, authors))


def extract_links(html):
    return re.findall(r'<a href="(.*?)"', html)


def extract_books_and_prices(html):
    book_titles = re.findall(r'<h3><a href=".*?" title="(.*?)">', html)
    book_prices = re.findall(r'<p class="price_color">£(.*?)</p>', html)
    return list(zip(book_titles, book_prices))

quotes_url = "http://quotes.toscrape.com/"
quotes_html = fetch_html(quotes_url)

quotes_and_authors = extract_quotes_and_authors(quotes_html)
print("Цитаты и их авторы:")
for quote, author in quotes_and_authors:
    print(f'"{quote}" — {author}')

links = extract_links(quotes_html)
print("\nСсылки на странице цитат:")
for i, link in enumerate(links, start=1):
    print(f"{i}: {link}")

books_url = "http://books.toscrape.com/"
books_html = fetch_html(books_url)

books_and_prices = extract_books_and_prices(books_html)
print("\nКниги и их цены:")
for title, price in books_and_prices:
    print(f'"{title}" — £{price}')
