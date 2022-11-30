import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Камень", paper: "Бумага", scissors: "Ножницы"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0


def start():
    print("Давайте сыграем в игру Камень, ножницы, бумага!")
    while game():
        pass
    score()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print()
        player = input("Камень = 1\nБумага = 2\nНожницы = 3\nДелай ход:")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Я не могу понять ваш выбор. Пожалуйста, введите 1, 2 или 3")


def result(player, computer):
    print("1...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.3)
    print("3!")
    time.sleep(0.2)
    print("Компьютер выбрал {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Ничья (ᵔ.ᵔ)")
    else:
        if rules[player] == computer:
            print("Вы победили! : )")
            player_score += 1
        else:
            print("Компьютер выиграл :(")


def play_again():
    answer = input("Желаете сыграть ещё раз? y/n: ")
    if answer in ("y", "Y", "Yes", "yes", "да", "Да"):
        return answer
    else:
        print("Спасибо за игру, увидимся в следующий раз!")


def score():
    global player_score, computer_score
    print("Итоговый счёт игры")
    print("Человек: ", player_score)
    print("Компьютер: ", computer_score)


if __name__ == "__main__":
    start()
