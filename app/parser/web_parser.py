import os
import re

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
            # словарь для временного хранения характеристик товаров
            dict_characters = {}

            link_feature = f"https://komp.1k.by{el_card.find('a').get('href')}"
            print(f'Получили ссылку {link_feature}')

            id_product = el_card.get('data-productid')
            print(f"Получили id товара {id_product}")

            # переход внутрь карточки товара
            request_features = requests.get(url=link_feature, headers=headers)
            response_features_bs = BeautifulSoup(request_features.text, 'lxml')

            name_model = response_features_bs.find('div', class_='heading')
            print(f'Получили модель {name_model}')
            price = response_features_bs.find('div', class_='spec-about__price')
            print(f'Получили цену {price}')

            dict_characters.update(id=id_product, Модель=name_model.text.strip(), Цена=price.text, Ссылка=link_feature)
            print(dict_characters)

            features = response_features_bs.find('div', class_='spec-info__main').find_all('tr', class_='spec-list__it')

            for feature in features:
                # получаем название характеристики
                name_character = feature.find('span', class_='spec-list__txt').text
                print(name_character)
                # получаем значение характеристики
                value_character = feature.find('td', class_='spec-list__val').text
                print(value_character)

                link_photos = response_features_bs.find_all('span', class_=re.compile('spec-images__it colorbox'))
                print(link_photos)
                download_image(id_product, link_photos)

        # следующая страница каталога
        number += 1

        next_page = bs.find('div', class_='paging__next')

        if not next_page:
            print('Завершили репарс всей категории, прекращаем выполнение')
            break


def download_image(id: str, photos: list):
    # путь к текущей директории + название папки по id
    directory = os.getcwd() + f'/results/{id}'
    # проверка есть ли текущая директория, создание при отсутствии
    if not os.path.exists(directory):
        os.makedirs(directory)

    for photo in photos:
        # извлечение ссылки
        link_photo = photo.get('data-srcbig')
        # получение id фотографии из ссылки
        # https://static.1k.by/images/productsimages/ip/big/ppa/0/4603926/iacd1a530a.jpg
        id_photo = link_photo.rsplit('/', 1)[1].split('.')[0]
        print(id_photo)
        path_save_photo = f'{directory}/{id_photo}.jpg'
        print(path_save_photo)
        result = requests.get(link_photo)
        # открыть файл для записи в бинарном формате
        with open(path_save_photo, 'wb') as img_file:
            img_file.write(result.content)


if __name__ == '__main__':
    request_get()
