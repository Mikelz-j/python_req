import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

url_list = open('url_list.txt', 'r')
list_prov = [i.strip() for i in url_list.readlines()]

lisk = open('list_isk.txt', 'r')
list_isk = [i.strip() for i in lisk.readlines()]

def response(url):
    req = requests.get(url, allow_redirects=False, timeout=5)
    if req.ok:
        return req

def response_code(url):
    return response(url).status_code


def find_url(url):
    href_list = []
    soup = BeautifulSoup(response(url).content, 'html.parser')
    items = soup.findAll('a')
    for item in items:
        href = str(item.get('href'))
        if href[0:2] == '//':
            url_a = 'http:' + href
            if url_a not in list_isk:
                href_list.append(url_a)
        elif href[0] == '/':
            url_a = 'https://seacomm.ru' + href
            if url_a not in list_isk:
                href_list.append(url_a)
        elif href[0:4] == 'http':
            if href not in list_isk:
                href_list.append(href)
    return href_list

def proverka(list_url):
    rez_list = []
    for url in list_url:
        print(url)
        if response_code(url) != 200:
            rez_list.append(url + ' - ' + str(response_code(url)))
        else:
            rez_list.append(url)
            rez_list.append('')
            for i in find_url(url):
                if response_code(i) != 200:
                    rez_list.append(i + ' - ' + str(response_code(i)))
        rez_list.append('')
        rez_list.append('<----------------------------------------->')
        rez_list.append('')
    r = open("rez.txt", "w")
    for i in rez_list:
        r.write(str(i) + '\n')
    r.close()

proverka(list_prov)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')