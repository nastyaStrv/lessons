from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from crud_functions import *
import asyncio

initiate_db()
add_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


inline_kb = InlineKeyboardMarkup(row_width=2)
inline_button_calculate = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_button_calculate, inline_button_formulas)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_calculate = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb.add(button_info)
kb.add(button_calculate)
kb.add(button_buy)

inline_kb_products = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    inline_kb_products.add(InlineKeyboardButton(text=f'Товар {i}', callback_data='product_buying'))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              'Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])

    man = 10 * weight + 6.25 * growth - 5 * age + 5
    woman = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Норма калорий для мужчин: {man}")
    await message.answer(f"Норма калорий для женщин: {woman}")

    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        product_name = product[0]
        product_description = product[1]
        product_price = product[2]
        await message.answer(f'Название: {product_name} | '
                             f'Описание: {product_description} | '
                             f'Цена: {product_price}')
        path = f'Images/Продукт_{i}.jpg'
        with open(path, 'rb') as img:
            await message.answer_photo(img)

    await message.answer('Выберите товар для покупки:', reply_markup=inline_kb_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)