import re

from bs4 import BeautifulSoup
import requests

host = 'https://komp.1k.by/mobile-notebooks/'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response_page = requests.get(url=host, headers=headers)

bs = BeautifulSoup(response_page.text, 'lxml')

print(bs.title.text)

# # получение всех объектов meta
# col_metas = bs.find_all('meta')
#
# for el_meta in col_metas:
#     # print(el_meta)
#     print(el_meta.get('content'))

# получение всех карточек товаров, class_ чтобы не путать с классом python
col_product = bs.find_all('div', class_='prod-nb')
print(len(col_product))

for el_product in col_product:
    id_product = el_product.get('data-seriesmainproductid')
    print(id_product)
    model = el_product.find('div', class_='prod-nb__head').find('span', class_='prod-nb__name')
    print(model.text.strip())
    price = el_product.find('div', class_='prod-nb__price')
    print(price.text)
    # получение ссылки на изображение с помощью маски
    link_image = el_product.find('span', class_=re.compile('colorbox_group')).get('data-srcbig')
    print(link_image)



