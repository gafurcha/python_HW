import requests
import re

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html_content = response.text

quotes = re.findall(r'<span class="text" itemprop="text">“(.*?)”</span>', html_content)
authors = re.findall(r'<small class="author" itemprop="author">(.*?)</small>', html_content)

print("Цитаты и их авторы:")
for quote, author in zip(quotes, authors):
    print(f'"{quote}" — {author}')

links = re.findall(r'<a href="(.*?)"', html_content)

print("\nСсылки на странице:")
for i, link in enumerate(links, start=1):
    print(f"{i}: {link}")
