from config import TOKEN
from config import db_pass
import psycopg2
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.utils import executor

bot = aiogram.Bot(token=TOKEN)
dp = Dispatcher(bot)

async def startup(_):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="car_rental",
            user="postgres",
            password=db_pass)
    except:
        print('Something gone wrong during connecting to the DataBase')
    else:
        print('Connection to DataBase sucessfully established')

@dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    bot.send_message(message.from_user.id, )

async def command_help(message : types.Message):
    bot.send_message(message.from_user.id, )


@dp.message_handler()
async def echo_reply(message : types.Message):
    await message.reply(f"Hello! I'm Your assistant. I like to chat with You, but please use command buttons to navigate.")












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
