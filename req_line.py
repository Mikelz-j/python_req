import requests
from urllib import request

post_url = 'https://stepic.org/media/attachments/course67/3.6.3/'

def response_don(url):
    return requests.get(url, allow_redirects=False).content

def obr(url):

    # Скачиваем файл по ссылке url и даем ему имя
    request.urlretrieve(url, "1.txt")

    # Открываем и читаем скаченый файл
    new_f = open('1.txt', 'r')
    str_f = [i.strip() for i in new_f.readlines()]
    return str_f

# Получаем url из файла
f = open('dataset_3378_3.txt', 'r')
url = f.read()
#print(url)
i = 0
while True:
    if obr(url)[0][-3:] != 'txt':
        print(obr(url))
        break
    else:
        i += 1
        print(obr(url)[0])
        url = post_url + obr(url)[0]
print(i)
#print(str_f[0][-4:])
