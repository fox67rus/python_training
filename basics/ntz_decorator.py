def decorator(count):
    def dec(function):
        import time
        def wrapper(*args, **kwargs):
            print(f'Запускаем функцию: {function}')
            start = time.time()
            for c in range(count):
                result = function(*args, **kwargs)
                print(f"{c} -{result}")
            finish = time.time()
            print(f"{function} завершила выполнение за {finish - start} секунд.")
            return result

        return wrapper
    return dec


@decorator(count=5)
def hello_world(name):
    hello_name = f'Hello, {name}'
    return hello_name


test = hello_world('Boris')
print(test)
