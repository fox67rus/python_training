from aiogram import Bot, Dispatcher, types
import asyncio

token = "5851531651:AAF0rxk4mRGCUAHLyUdw_QjeiDSNJkJiCG8"

async def echo(message: types.Message):
    print(f"Получено сообщение: {message.text}")
    # метод ответ
    await message.answer(message.text)


async def start():
    bots = Bot(token)
    dp = Dispatcher()

    # регистрация хэндлеров
    dp.message.register(echo)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())


