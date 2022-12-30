count = 0

while count < 5:

    try:
        age = int(input("Введите ваш возраст: "))
        print(f"Вы ввели {age} лет")
        break
    except ValueError as e:
        print(f"Вы ввели некорректное значение - {e}")
    except:
        print("Неизвестная ошибка")

    count +=1



