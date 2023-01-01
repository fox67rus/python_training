from bs4 import BeautifulSoup
import requests

host = 'https://komp.1k.by/mobile-notebooks/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response_page = requests.get(url=host, headers=headers)

bs = BeautifulSoup(response_page.text, 'lxml')

print(bs.title.text)

# получение всех объхектов meta
col_metas = bs.find_all('meta')

for el_meta in col_metas:
    # print(el_meta)
    print(el_meta.get('content'))

