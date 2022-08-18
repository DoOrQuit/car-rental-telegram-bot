from config import TOKEN
from config import db_pass
import psycopg2
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram import types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from core.packages import kb_pack as kb


bot = aiogram.Bot(token=TOKEN)
dp = Dispatcher(bot)

#async def startup(_):
    #try:
        #conn = psycopg2.connect(
            #database="car_rental",
            #user="postgres",
            #password=db_pass)
    #except:
        #print('Something gone wrong during connecting to the DataBase')
    #else:
        #print('Connection to DataBase sucessfully established')

@dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Fine. Let's start!", reply_markup= kb.main_buttons)

async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, "You pressed a Help button", reply_markup= kb.main_buttons)

@dp.message_handler(commands = ['contacts'])
async def command_contacts(message : types.Message):
    await bot.send_message(message.from_user.id, "b.125 Myra Street, Kyiv\nPhone Number : +380123456789"
                                                "\nemail: test@rentals.ua", reply_markup=kb.main_buttons)




@dp.message_handler()
async def echo_reply(message : types.Message):
    await message.reply(f"Hello! I'm Your assistant. I like to chat with You, but please use command buttons to navigate.")












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
