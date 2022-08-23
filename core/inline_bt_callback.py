import aiogram
import asyncio
import psycopg2
from aiogram import types
from main import bot, dp


# @dp.callback_query_handler(func=lambda c: c.data == 'economy_cars_show')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')