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

from db.database import Session
from db.models.names import (
    NameExpense,
    NameIncome,
)

from pagination.kb import InlineKeyboardPaginator


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

# Scrolling pages
@dp.callback_query_handler(
    lambda c: 'name_income' in c.data.split('#')[0])
async def name_income_pages(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await start_adding_income(
        call.message,
        page)


@dp.callback_query_handler(
    lambda c: 'name_expense' in c.data.split('#')[0])
async def name_income_pages(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await start_adding_expense(
        call.message,
        page)


# My functions

async def start_adding_income(message: types.Message, page=1):
    session = Session()
    names = [(name.id, name.name) for name in session.query(NameIncome).all()]

    if len(names) % 10 == 0:
        pages = len(names)//10
    else:
        pages = len(names)//10 + 1

    paginator = InlineKeyboardPaginator(
        pages,
        current_page=page,
        data_pattern='name_income#{page}',
    )

    start_for = page * 10 - 10
    stop_for = page * 10
    if len(names) < stop_for:
        stop_for = len(names)
    for i in range(start_for, stop_for, 2):
        if stop_for != (i + 1):
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=names[i][0]),
                InlineKeyboardButton(
                    names[i+1][1],
                    callback_data=names[i+1][0]))
        else:
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=names[i][0]))

    await message.answer(
        text=f'Откуда доход?',
        reply_markup=paginator.markup)


async def start_adding_expense(message: types.Message, page=1):
    session = Session()
    names = [(name.id, name.name) for name in session.query(NameExpense).all()]

    if len(names) % 10 == 0:
        pages = len(names)//10
    else:
        pages = len(names)//10 + 1

    paginator = InlineKeyboardPaginator(
        pages,
        current_page=page,
        data_pattern='name_expense#{page}',
    )

    start_for = page * 10 - 10
    stop_for = page * 10
    if len(names) < stop_for:
        stop_for = len(names)
    for i in range(start_for, stop_for, 2):
        if stop_for != (i + 1):
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=names[i][0]),
                InlineKeyboardButton(
                    names[i+1][1],
                    callback_data=names[i+1][0]))
        else:
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=names[i][0]))

    await message.answer(
        text=f'На что потрачено?',
        reply_markup=paginator.markup)


#Message Handlers

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


@dp.message_handler()
async def message_parser(message: types.Message):
    if message.text == 'Бюджет':
        await message.reply('Бюджет')
    elif message.text == 'Добавить Доходы':
        await start_adding_income(message, 1)
    elif message.text == 'Добавить Расходы':
        await start_adding_expense(message)
#    elif message.text == 'Добавить Активы':
#        await start_adding_asset(message):
#    elif message.text == 'Добавить Пассивы':
#        await start_adding_liabilities(message)
    else:
        await message.reply('Не понял')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
