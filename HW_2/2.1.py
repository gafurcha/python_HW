import requests
import re

url = "http://quotes.toscrape.com/"
response = requests.get(url)

html_content = response.text

quotes = re.findall(r'<span class="text" itemprop="text">“(.*?)”</span>', html_content)

authors = re.findall(r'<small class="author" itemprop="author">(.*?)</small>', html_content)

for i in range(len(quotes)):
    print(f'"{quotes[i]}" — {authors[i]}')
