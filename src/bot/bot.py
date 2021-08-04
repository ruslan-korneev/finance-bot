from asgiref.sync import sync_to_async
import asyncio
import logging
import os


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup


# Configure logging
logging.basicConfig(
        filename='bot.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')

# Telegram token from Bot Father
TG_TOKEN = os.environ.get('TG_TOKEN')

# Initialize bot and dispatcher
bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# Start with hello message
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    reply = "-"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    budget_button = types.KeyboardButton('Бюджет')
    add_income_button = types.KeyboardButton('Добавить Доходы')
    add_expenses_button = types.KeyboardButton('Добавить Расходы')
    add_assets_button = types.KeyboardButton('Добавить Активы')
    add_liabilities_button = types.KeyboardButton('Добавить Пассивы')
    keyboard.row(budget_button)
    keyboard.row(
        add_income_button, add_expenses_button)
    keyboard.row(
        add_assets_button, add_liabilities_button)
    await message.reply(reply, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
