# 1. Приветствие
# 2. Выдача мануала игры
# 3. Создание русско-английского словаря
# 4. Описание алгоритма сбора слов
# 4.1. Сбор 4х образцов (произвольно) -> Машина, Ракета, Школа, Привет
# 4.2. Сбор 1 слова, которое является вопросом -> Ракета
# 4.3. Задать вопрос игроку -> переведите "Ракета"
# 4.4. Вывод на экран вариантов ответов
# 5. Получение ответа от игрока
# 6. Сравнение ответов и выдача ответа машины
# ДЗ
# Защита от выхода за пределы списка random_words
# Инверсия словаря по выбору игрока
# Выбор уровня сложности
import random

print("Привет, игрок!")  # 1

print("Вам будет дано слово на русском языке и 4 варианта ответов на "
      "английском. Выберите самый подходящий вариант!")  # 2

WORDS = {
    'Привет': 'Hello',
    'Пока': 'Goodbye',
    'Запустить': 'Run',
    'Ракета': 'Rocket',
    'Школа': 'School',
    'Змея': 'Python',
    'Машина': 'Car',
    'Язык': 'Language'
}  # 3

print(list(WORDS.keys()))
random_words = random.sample(WORDS.keys(), 4)  # 4.1.

random_word = random.choice(random_words)  # 4.2.

print(f'Переведите слово "{random_word}" на английский язык')  # 4.3.

for i, word in enumerate(random_words, start=1):
    print(f'{i}. {WORDS[word]}')  # 4.4.

player_answer = int(input('Введите ответ: '))  # 5.

if random_words[player_answer - 1] == random_word:  # 6.
    print('Верно!')
else:
    print(f'Не верно! Правильный ответ: {WORDS[random_word]}')

