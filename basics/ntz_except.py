count = 0

while count < 5:

    try:
        num = int(input("Введите первое число: "))
        print(f"Вы ввели {num} лет")
        break
    except ValueError as e:
        print(f"Вы ввели некорректное значение - {e}")
    except:
        print("Неизвестная ошибка")

    count += 1
