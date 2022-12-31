from aiogram import Bot, Dispatcher, types
import asyncio
import logging

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


async def start():
    # включение логирования
    logging.basicConfig(
        level=logging.INFO
    )
    logger.error("Error")

    bots = Bot(token)
    dp = Dispatcher()

    # регистрация хэндлеров
    dp.message.register(echo)
    dp.startup.register(start_up)
    dp.shutdown.register(shut_down)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())
