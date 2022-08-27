import asyncio
from config import TOKEN
from config import db_pass
from datetime import date, datetime
import psycopg2
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from core.packages import kb_pack as kb


bot = aiogram.Bot(token=TOKEN)
dp = Dispatcher(bot)
current_time = datetime.now().strftime("%H%M")
connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)

@dp.message_handler(commands = ['start'])
async def command_start(message : types.Message):
    if 1200 > int(current_time) > 0000 :
        await bot.send_message(message.from_user.id, f"Good morning, {message.from_user.first_name}."
                                                    " Please, press one of the buttons below \U00002B07", reply_markup= kb.main_buttons)
    elif 1600 > int(current_time) > 1200 :
        await bot.send_message(message.from_user.id, f"Good afternoon, {message.from_user.first_name}."
                                                    " Please, press one of the buttons below \U00002B07", reply_markup= kb.main_buttons)
    elif 2359 > int(current_time) > 1600 :
        await bot.send_message(message.from_user.id, f"Good evening, {message.from_user.first_name}."
                                                    " Please, press one of the buttons below \U00002B07", reply_markup= kb.main_buttons)

@dp.message_handler(commands = ['help'])
async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, "Don't worry. We'll assist You with any problem", reply_markup= kb.help_buttons)

@dp.message_handler(commands = ['contacts'])
async def command_contacts(message : types.Message):
    await bot.send_message(message.from_user.id, "Office address: b.125 Myra Street, Kyiv\nPhone Number: +380123456789"
                                                "\nEmail: test@rentals.ua", reply_markup=kb.main_buttons)



@dp.message_handler(lambda message : 'assistant' in message.text.lower())
async def assistant_contact(message : types.Message):
    await message.reply("Customers support contact 24/7\n+380991234567")
    await bot.send_message(message.from_user.id,'Hope I could help', reply_markup=kb.main_buttons)



"""Identifies the category for building the class object and branching the dialog relating to renting filters"""
@dp.message_handler(lambda message : 'rent' in message.text.lower())
async def category_identifier(message : types.Message):
    await message.reply("Sure! We'll find a perfect car for You!")
    await asyncio.sleep(2)
    await bot.send_message(message.from_user.id,"Please, use the menu \U00002B07 to find Your perfect car,"
                                                " or send me message with the brand/model You like", reply_markup=kb.category_buttons)
    

@dp.message_handler(lambda message : 'economy' in message.text.lower())
async def economy_category(message : types.Message):
    await message.reply('Economy category\n(15$ - 45$)\nPlease, use the buttons to navigate \U00002B07',reply_markup=kb.economy_inline_filters_buttons)

@dp.callback_query_handler(text='economy_cars_show')
async def economy_filters_inline(callback: types.CallbackQuery):
    await callback.message.answer("Brands available in this category \U00002B07", reply_markup=kb.economy_brands_inline)

        
        

@dp.message_handler()
async def echo_reply(message : types.Message):
    await message.reply("Hello! I'm Your assistant. Probably I didn't understand you." 
                        " Please repeat Your question.")














if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
