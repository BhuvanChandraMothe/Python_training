from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

def fetch(url):
    response = requests.get(url)
    return response.text

def parsehtml(html):
    page = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in page.find_all('a', href = True)]
    return links

def fetchandparse(url):
    html = fetch(url)
    links = parsehtml(html)
    print(links)


if __name__ == '__main__':
    url = "https://docs.python.org/3/"
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetchandparse, url) for _ in range(5)]
    for future in futures:
        future.result()