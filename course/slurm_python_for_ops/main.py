import json
import requests


def main():
    base_url = 'https://httpbin.org'

    query_params = {
        'param1': 'foo',
        'param2': 'bar',
    }

    headers = {
        'User-Agent': 'Chrome',
        'Authorization': 'Bearer: tokenblablabla'
    }
    payload = {
        'id': '12345',
        'name': 'python'
    }

    # response = requests.get(base_url + '/get', params=query_params,
    #                         headers=headers)
    with open('load.txt') as text_file:
        files = {
            'text_file': text_file
        }

        try:
            response = requests.post(url=base_url + '/post',
                                     params=query_params,
                                     headers=headers,
                                     data=payload,
                                     files=files,
                                     timeout=0.001)
        except requests.exceptions.ConnectTimeout:
            print(f'Ресурс {base_url} недоступен')
        else:
            print(response.status_code)
            # print(response.text)
            print(response.json())
            # преобразование json в словарь и словарь в json
            print(json.dumps(json.loads(response.text)))


if __name__ == '__main__':
    main()
