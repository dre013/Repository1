import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html')
title = soup.find_all('h2', {'class': 'post-title'})

list_with_results = []

for t in title:
    results = t.getText(strip = True)
    list_with_results.append(results)

print(list_with_results)