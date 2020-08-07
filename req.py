import urllib3
import certifi
print(urllib3.PoolManager(ca_certs=certifi.where()).request('GET', 'https://landcomm.ru/catalog/307/13873/').status)