from bs4 import BeautifulSoup
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
              '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/108.0.0.0 Safari/537.36'
}

proxy = '1.1.1.1:8080'
auth_proxy = 'login:password'

proxies = {
    'https': f'http://{auth_proxy}@{proxy}'
}

host = 'https://komp.1k.by/mobile-notebooks/s.php?alias=mobile&alias2=notebooks&filter=actual&viewmode=table&page='


# формирование запроса с учетом нумерации страниц
def request_get():
    number = 1

    while True:
        url = f'{host}{number}'

        # response_page = requests.get(url=url, headers=headers, proxies=proxies)
        response_page = requests.get(url=url, headers=headers)

        bs = BeautifulSoup(response_page.text, 'lxml')

        # создаем коллекцию карточек товаров
        col_cards = bs.find_all('div', class_='prod-cell')
        print(f'На странице {number} найдено {len(col_cards)} товаров')

        # перебор карточек и получение ссылок на товары
        for el_card in col_cards:
            link_feature = f"https://komp.1k.by{el_card.find('a').get('href')}"
            print(f'Получили ссылку {link_feature}')

            id_product = el_card.get('data-productid')
            print(f"Получили id товара {id_product}")

        # следующая страница каталога
        number += 1

        next_page = bs.find('div', class_='paging__next')

        if not next_page:
            print('Завершили репарс всей категории, прекращаем выполнение')
            break


if __name__ == '__main__':
    request_get()
