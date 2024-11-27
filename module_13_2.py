import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types

api = '7898759014:AAG4Nuv9SI0789X4S_n6VEpoaWR93-lf5pY'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

