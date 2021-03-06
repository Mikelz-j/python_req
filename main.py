import requests
from bs4 import BeautifulSoup
from time import time

tic = time()

url_site = open('url.txt', 'r').read()
if url_site[-1] == '/':
    chif_url = url_site[0:-1]
else:
    chif_url = url_site

url_list = open('url_list.txt', 'r')
list_prov = [i.strip() for i in url_list.readlines()]

lisk = open('list_isk.txt', 'r')
list_isk = [i.strip() for i in lisk.readlines()]

def write_result(str):
    r = open("rez.txt", "a")
    r.write(str + '\n')
    r.close()

def response(url):
    req = requests.get(url, allow_redirects=False, verify=True)
    if req.ok:
        return req

def response_code(url):
    try:
        return response(url).status_code
    except:
        return 'Error'


url_dist = {}

def find_url(url):
    href_list = []
    href_list_out = []
    soup = BeautifulSoup(response(url).content, 'html.parser')
    items = soup.findAll('a')
    for item in items:
        href = str(item.get('href'))
        if href[0:2] == '//':
            if href[2:5] != 'www':
                url_a = 'https:' + href
                if url_a not in list_isk:
                    href_list.append(url_a)
        elif href[0] == '/':
            url_a = chif_url + href
            if url_a not in list_isk:
                href_list.append(url_a)
        elif href[0:4] == 'http':
            if href not in list_isk:
                href_list.append(href)
    return href_list

def proverka(list_url):
    for url in list_url:
        print(url)
        if response_code(url) != 200:
            write_result(url + ' - ' + str(response_code(url)))
        else:
            write_result(url)
            write_result('')
            for i in find_url(url):
                if response_code(i) != 200:
                    write_result(i + ' - ' + str(response_code(i)))
        write_result('')
        write_result('<----------------------------------------->')
        write_result('')

proverka(list_prov)

print('Ok')
toc = time()
print(str(round((toc - tic), 1)) + ' sec')