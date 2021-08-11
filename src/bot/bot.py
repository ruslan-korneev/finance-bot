import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from db.database import Session
from db.models.names import (
    NameExpense,
    NameIncome,
    NameAsset,
    NameLiability,
)
from db.models.incomes import Income
from db.models.expenses import Expense
from db.models.assets import Asset
from db.models.liabilities import Liability

from pagination.kb import InlineKeyboardPaginator

from forex_python.converter import CurrencyRates

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

CURRENCY_CHOICES = (
    ('RUB', 'RUB'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('CZK', 'CZK'),
)


class Form(StateForm):
    amount = State()


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
async def name_expense_pages(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await start_adding_expense(
        call.message,
        page)


@dp.callback_query_handler(
    lambda c: 'name_asset' in c.data.split('#')[0])
async def name_asset_pages(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await start_adding_asset(
        call.message,
        page)


@dp.callback_query_handler(
    lambda c: 'name_liability' in c.data.split('#')[0])
async def name_liability_pages(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await start_adding_liability(
        call.message,
        page)


@dp.callback_query_handler(
    lambda c: 'income_id' in c.data.split('#')[0])
async def set_income_currency(call):
    income_id = int(call.data.split('#')[1])
    reply = 'Выбери валюту...'
    currency = CURRENCY_CHOICES
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    for i in range(0, 3, 2):
        keyboard.add(
            InlineKeyboardButton(
                text=currency[i][0],
                callback_data=currency[i][1]),
            InlineKeyboardButton(
                text=currency[i+1][0],
                callback_data=currency[i+1][1]))
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=reply,
        reply_markup=keyboard)


@dp.callback_query_handler(
    lambda c: any(c.data in cur for cur in CURRENCY_CHOICES))
async def set_amount_of_income(call, name_id):
    reply = 'Напишите, сколько денег пришло...'
    await bot.send_message(reply)
    await Form.amount.set()

@dp.message_handler(state=Form.url)
async def process_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as amount:
        amount['amount'] = message.text
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
    c_data = 'income_id#'
    start_for = page * 10 - 10
    stop_for = page * 10
    if len(names) < stop_for:
        stop_for = len(names)
    for i in range(start_for, stop_for, 2):
        if stop_for != (i + 1):
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=c_data+str(names[i][0])),
                InlineKeyboardButton(
                    names[i+1][1],
                    callback_data=c_data+str(names[i+1][0])))
        else:
            paginator.add_before(
                InlineKeyboardButton(
                    names[i][1],
                    callback_data=c_data+str(names[i][0])))

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


async def start_adding_asset(message: types.Message, page=1):
    session = Session()
    names = [(name.id, name.name) for name in session.query(NameAsset).all()]

    if len(names) % 10 == 0:
        pages = len(names)//10
    else:
        pages = len(names)//10 + 1

    paginator = InlineKeyboardPaginator(
        pages,
        current_page=page,
        data_pattern='name_asset#{page}',
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
        text=f'Какие активы приобрели?',
        reply_markup=paginator.markup)


async def start_adding_liability(message: types.Message, page=1):
    session = Session()
    names = [(name.id, name.name) for name in session.query(NameLiability).all()]

    if len(names) % 10 == 0:
        pages = len(names)//10
    else:
        pages = len(names)//10 + 1

    paginator = InlineKeyboardPaginator(
        pages,
        current_page=page,
        data_pattern='name_liability#{page}',
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
        text=f'...опять пассивы?\nИ какие же?...',
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


async def send_budget(message: types.Message):
    session = Session()

    if session.query(Income).count() > 0:
        inc = session.query(Income).with_entities(Income.amount, Income.currency).all()
    else:
        inc = [(0, 'RUB')]
    if session.query(Expense).count() > 0:
        exp = session.query(Expense).with_entities(Expense.amount, Expense.currency).all()
    else:
        exp = [(0, 'RUB')]
    if session.query(Asset).count() > 0:
        ass = session.query(Asset).with_entities(Asset.amount, Asset.currency).all()
    else:
        ass = [(0, 'RUB')]
    if session.query(Liability).count() > 0:
        liab = session.query(Liability).with_entities(Liability.amount, Liability.currency).all()
    else:
        liab = [(0, 'RUB')]

    budget = 0

    for amount, currency in inc:
        if currency != 'RUB':
            c = CurrencyRates
            rate = c.get_rate(currency, 'RUB')
            amount = amount * rate
        budget += amount
    objs = (exp, ass, liab)
    for obj in objs:
        for amount, currency in obj:
            if currency != 'RUB':
                c = CurrencyRates()
                rate = c.get_rate(currency, 'RUB')
                amount = amount * rate
            budget -= amount
    reply = f'У вас должно быть {round(budget, 2)} RUB'
    await message.answer(reply)


@dp.message_handler()
async def message_parser(message: types.Message):
    if message.text == 'Бюджет':
        await send_budget(message)
    elif message.text == 'Добавить Доходы':
        await start_adding_income(message, 1)
    elif message.text == 'Добавить Расходы':
        await start_adding_expense(message)
    elif message.text == 'Добавить Активы':
        await start_adding_asset(message)
    elif message.text == 'Добавить Пассивы':
        await start_adding_liability(message)
    else:
        await message.reply('Не понял')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
