"""
1- Подключение к телеграм через пакеты 
2- Создать телеграмм бота через @BotFather
3- Получить секретный ключ доступа к нашему боту
4- Подключить наш бот к Python 
5- Написать приветствие + мануал когда пользовательно пишет \start
6- Игра
"""

import random

from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters
from telegram import ReplyKeyboardMarkup


SECRET_KEY = '5706857193:AAG46KIh0Vkrk4FfB0Q-ARh_Kf9Ee9sdxcU'

WORDS = {
  'Привет': 'Hello',
  'Пока': 'Goodbye',
  'Запустить': 'Run',
  'Ракета': 'Rocket',
  'Школа': 'School',
  'Змея': 'Python',
  'Машина': 'Car',
  'Язык': 'Language'
}


def generate_question():
  options = random.sample(WORDS.keys(), 4)
  question = random.choice(options)
  correct_answer = WORDS[question]
  return options, question, correct_answer

# randomizer = generate_question()
# translate_randomizer = []

# for item in randomizer[0]:
#   translate_randomizer.append(WORDS[item])

# print(randomizer[0])
# print(translate_randomizer)

def handle_start(update, context):
  chat_id = update.effective_chat.id
  context.bot.send_message(chat_id=chat_id,
                           text='Привет!')
  context.bot.send_message(chat_id=chat_id,
                          text="Вам будет дано слово на русском, и 4 варианта его перевода на английском языке. Выберите наиболее подходящий на ваш взгляд")
  updater(update, context)
  

def handle_answer(update, context):
  chat_id = update.effective_chat.id
  player_answer = update.effective_message.text
  correct_answer = context.user_data['answer']
  if correct_answer == player_answer:
    context.bot.send_message(chat_id=chat_id,
                       text='Правильно!')
  else:
    context.bot.send_message(chat_id=chat_id,
                       text=f'Неправильно! правильный ответ: {correct_answer}')

  updater(update, context)


def updater(update, context):
  chat_id = update.effective_chat.id
  options, question, correct_answer = generate_question()

  translate_options = []
  for item in options: # Ракета -> Змея -> Язык...
    translate_options.append(WORDS[item])

  keyboard = ReplyKeyboardMarkup.from_column(
    translate_options,
    one_time_keyboard=True,
    resize_keyboard=True,
  )
  context.bot.send_message(chat_id=chat_id,
                          text=f'Переведите слово "{question}"',
                          reply_markup=keyboard)
  context.user_data['answer'] = correct_answer
  

bot = Updater(token=SECRET_KEY)
# /start -> Приветствие
bot.dispatcher.add_handler(CommandHandler('start', handle_start))
# Начало игры
bot.dispatcher.add_handler(MessageHandler(Filters.text, handle_answer))

bot.start_polling()