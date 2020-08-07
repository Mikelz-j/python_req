import requests

print(requests.get('https://pddimp.yandex.ru/api2/admin/email/list?domain=seacomm.ru&page=1&on_page=5 HTTP/1.1').content)