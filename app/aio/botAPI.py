from aiogram import Bot, Dispatcher, types, F
import asyncio
import logging
import settings

from aiogram.filters import Text, Command
from aiogram.types import BotCommand, BotCommandScopeDefault

token = settings.TOKEN
admin_id = settings.ADMIN_ID

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


async def hi_admin(message: types.Message):
    await message.reply("Привет, админ!")

# обработка картинок
# async def pictures(message: types.Message):
#     await message.answer("Привет! Красивая картинка")


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

    # dp.message.register(pictures, content_types=['photo', 'sticker'])
    # приветствие админа
    dp.message.register(hi_admin, F.from_user.id == admin_id, F.text == 'Привет')
    # обработка команд
    dp.message.register(on_start, Command(commands=['start', 'go']))
    # регистрация хэндлера с фильтром
    dp.message.register(text, Text(text='Салют'))
    dp.message.register(echo)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())
