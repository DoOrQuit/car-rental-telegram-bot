import asyncio
from cgitb import text
from config import TOKEN
from datetime import datetime
import psycopg2
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from core.buttons_pack import essential_bt as kb
from core.buttons_pack import car_category_bt as ct_kb
from core.buttons_pack.bt_generators.model_button_generator import economy_mdls_bt_generator




bot = aiogram.Bot(token=TOKEN)
dp = Dispatcher(bot)
current_time = datetime.now().strftime("%H%M")

"""Start Command"""
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

"""Help Command"""
@dp.message_handler(commands = ['help'])
async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, "Don't worry. We'll assist You with any problem", reply_markup= kb.help_buttons)

"""Contacts Command"""
@dp.message_handler(commands = ['contacts'])
async def command_contacts(message : types.Message):
    await bot.send_message(message.from_user.id, "Office address: b.125 Myra Street, Kyiv\nPhone Number: +380123456789"
                                                "\nEmail: test@rentals.ua", reply_markup=kb.main_buttons)


"""Assistant Call. Reacts for text in chat"""
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
    

"""Economy Section of message and callback handlers"""
@dp.message_handler(lambda message : 'economy' in message.text.lower())
async def economy_category(message : types.Message):
    await message.reply('Economy category\n(15$ - 45$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.economy_inline_filters_buttons)

@dp.callback_query_handler(text='economy_cars_show')
async def economy_cars_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.economy_brands_inline)


@dp.callback_query_handler(Text(startswith='economy_'))
async def economy_models_inline(callback: types.CallbackQuery):
    brand_choosen = callback.data.split('_')
    await callback.message.reply("Models available \U00002B07", reply_markup=economy_mdls_bt_generator(brand_choosen[1]))

# @dp.callback_query_handler(Text(startswith='ecnm_'))
# async def ecnm_model_info(callback: types.CallbackQuery):
#     #model_ident = (callback.data.split('_'))[]
    









@dp.message_handler(lambda message : 'middle' in message.text.lower())
async def middle_category(message : types.Message):
    await message.reply('Middle category\n(30$ - 70$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.middle_inline_filters_buttons)

@dp.callback_query_handler(text='middle_cars_show')
async def middle_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.middle_brands_inline)

@dp.message_handler(lambda message : 'business' in message.text.lower())
async def business_category(message : types.Message):
    await message.reply('Business category\n(43$ - 90$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.business_inline_filters_buttons)

@dp.callback_query_handler(text='business_cars_show')
async def business_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.business_brands_inline)

@dp.message_handler(lambda message : 'premium' in message.text.lower())
async def premium_category(message : types.Message):
    await message.reply('Premium category\n(Starts from 85$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.premium_inline_filters_buttons)

@dp.callback_query_handler(text='premium_cars_show')
async def premium_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.premium_brands_inline)

@dp.message_handler(lambda message : 'suv' in message.text.lower())
async def suv_category(message : types.Message):
    await message.reply('Suv category\n(Starts from 36$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.suv_inline_filters_buttons)

@dp.callback_query_handler(text='suv_cars_show')
async def suv_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.suv_brands_inline)

@dp.message_handler(lambda message : 'minivan' in message.text.lower())
async def minivan_category(message : types.Message):
    await message.reply('Minivan category\n(Starts from 33$)\n'
                        'Please, use the buttons to navigate \U00002B07',reply_markup=ct_kb.minivan_inline_filters_buttons)

@dp.callback_query_handler(text='minivan_cars_show')
async def minivan_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands available in this category \U00002B07", reply_markup=ct_kb.minivan_brands_inline)

      
        
"""Common echo replier"""
@dp.message_handler()
async def echo_reply(message : types.Message):
    await message.reply("Hello! I'm Your assistant. Probably I didn't understand you." 
                        " Please repeat Your question.")








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
