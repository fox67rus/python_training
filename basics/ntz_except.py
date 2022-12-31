count = 0

while count < 5:

    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        if num2 == 0:
            # выброс исключения
            raise ZeroDivisionError('Делить на ноль не допустимо')

        result = num1 / num2

        # print(f"Вы ввели {num} лет")
        # break
    except ValueError as e:
        print(f"Вы ввели некорректное значение - {e}")

    except ZeroDivisionError as z:
        print('Делить на ноль нельзя!')
        print(f'{z}')
    except:
        print("Неизвестная ошибка")

    # блок кода выполнится в любом случае - для закрытия файлов и освобождения ресурсов
    finally:
        print('finaly')

    count += 1
