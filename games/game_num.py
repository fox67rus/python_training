import random


def start_game():
    random_number = random.randint(1, 5)
    user_number = input("Угадай число (от 1 до 5): ")

    if int(user_number) == random_number:
        print(f"Вы угадали! Это {random_number}")
    else:
        print(f"Вы не угадали, это {random_number}")
    # break # выход из цикла, если действия прошли успешно


if __name__ == '__main__':
    while True:
        try:
            start_game()
        except:
            print("Error!")
