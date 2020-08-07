import requests
from urllib import request
#from time import time
#tic = time()

def response_don(url):
    return requests.get(url, allow_redirects=False).content

# Получаем url из файла
f = open('dataset_3378_2.txt', 'r')
url = f.read()

# Скачиваем файл по ссылке url и даем ему имя
request.urlretrieve(url, "1.txt")

# Открываем и читаем скаченый файл
new_f = open('1.txt', 'r')
str_num = [i.strip() for i in new_f.readlines()]
print(len(str_num))

#toc = time()
#print(str(round((toc - tic), 1)) + ' sec')