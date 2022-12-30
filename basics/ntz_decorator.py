def decorator(function):
   import time
   def wrapper():
        print(f'Запускаем функцию: {function}')
        start = time.time()
        function()
        finish = time.time()
        print(f'{function} завершила выполнение за {finish - start} секунд.')

    # возвращаем обертку
    return wrapper

@decorator
def hello_world():
    print('Hello World!')

hello_world()