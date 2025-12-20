from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

url = 'https://es.wikipedia.org/wiki/Web_scraping'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("REQUEST SUCCESSFUL")
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = [title.string for title in soup.find_all('h2')]
    print(titles)

    links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]
    print(links)
else: print("ERROR")