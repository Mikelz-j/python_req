import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

def response(url):
    return requests.get(url)

def find_url(url):
    href_list = []
    soup = BeautifulSoup(response(url).content, 'html.parser')
    items = soup.findAll('a')
    for item in items:
        href = str(item.get('href'))
        if href[0] == '/':
            href_list.append('https://seacomm.ru' + href)
        elif href[0:4] == 'http':
            href_list.append(href)
    return href_list

def response_code(url):
    return requests.get(url, allow_redirects=False).status_code

def proverka(list_url):
    for url in list_url:
        print(url)
        for i in find_url(url):
            if response_code(i) != 200:
                print(i, end=' - ')
                print(response_code(i))
        print('/************************************************/')
    print('Ok')

list_prov = [
'https://seacomm.ru/catalog/29/',
'https://seacomm.ru/catalog/50/1009/',
'https://seacomm.ru/dokumentacija/12462/'
]

proverka(list_prov)

toc = time()
print(str(round((toc - tic), 1)) + ' sec')