from aiogram import Bot, Dispatcher, types
import asyncio
import logging

from aiogram.filters import Text, Command
from aiogram.types import BotCommand, BotCommandScopeDefault

token = "5851531651:AAF0rxk4mRGCUAHLyUdw_QjeiDSNJkJiCG8"
admin_id = 924348820

logger = logging.getLogger(__name__)


# создание команд
async def commands(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        )
    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())


async def start_up(bot: Bot):
    await commands(bot)
    await bot.send_message(admin_id, text="Бот запущен")


async def shut_down(bot: Bot):
    await bot.send_message(admin_id, text="Бот выключен")


async def echo(message: types.Message):
    print(f"Получено сообщение: {message.text}")
    # метод ответ
    await message.answer(message.text)


async def text(message: types.Message):
    await message.answer("Ты ввел текст: " + message.text)

async def on_start(message: types.Message):
    await message.reply("Начинаем работать")


async def start():
    # включение логирования
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")

    bots = Bot(token)
    dp = Dispatcher()

    # регистрация хэндлеров
    dp.startup.register(start_up)
    dp.shutdown.register(shut_down)

    # регистрация хэндлера с фильтром
    dp.message.register(on_start, Command(commands=['start', 'go']))
    dp.message.register(text, Text(text='Салют'))
    dp.message.register(echo)


    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())
