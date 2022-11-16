from config import TOKEN
from core.car_info_img.img_attacher import img_loader
from datetime import datetime  # imported for defining the current time for initial greetings during bot activation.
import aiogram
from aiogram import Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from core import essential_bt as kb
from core import car_category_bt as ct_kb
from core.model_list_generator import *
from core.model_button_generator import mdls_bt_generator
from core.brand_button_generator import brands_bt_generator
from core.car_info_img.model_info import car_info


bot = aiogram.Bot(token=TOKEN)
dp = Dispatcher(bot)
current_time = datetime.now().strftime("%H%M")

"""Start Command"""


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if 1200 > int(current_time) > 0000:
        await bot.send_message(message.from_user.id, f"Good morning, {message.from_user.first_name}."
                                                     " Please, press one of the buttons below \U00002B07",
                               reply_markup=kb.main_buttons)
    elif 1600 > int(current_time) > 1200:
        await bot.send_message(message.from_user.id, f"Good afternoon, {message.from_user.first_name}."
                                                     " Please, press one of the buttons below \U00002B07",
                               reply_markup=kb.main_buttons)
    elif 2359 > int(current_time) > 1600:
        await bot.send_message(message.from_user.id, f"Good evening, {message.from_user.first_name}."
                                                     " Please, press one of the buttons below \U00002B07",
                               reply_markup=kb.main_buttons)
    
    brands_list_gen('economy')   # initialization and generation the list of brands fetched from Database
    brands_list_gen('middle')
    brands_list_gen('business')
    brands_list_gen('premium')
    brands_list_gen('suv')
    brands_list_gen('minivan')


"""Help Command"""


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Don't worry. We'll assist You with any problem",
                           reply_markup=kb.help_buttons)

"""Contacts Command"""


@dp.message_handler(commands=['contacts'])
async def command_contacts(message: types.Message):
    await bot.send_message(message.from_user.id, "Office address: b.125 Myra Street, Kyiv\nPhone Number: +380123456789"
                                                 "\nEmail: test@rentals.ua",
                           reply_markup=kb.main_buttons)

"""Assistant Call. Reacts for text in chat"""


@dp.message_handler(lambda message: 'assist' in message.text.lower())   # bot reaction for word 'assist' in message
async def assistant_contact(message: types.Message):
    await message.reply("Customers support contact 24/7\n+380991234567")
    await bot.send_message(message.from_user.id, 'Hope I could help', reply_markup=kb.main_buttons)


@dp.message_handler(lambda message: 'help' in message.text.lower())  # bot reaction for word 'help' in message
async def assistant_contact(message: types.Message):
    await message.reply("Customers support contact 24/7\n+380991234567")
    await bot.send_message(message.from_user.id, 'Hope I could help', reply_markup=kb.main_buttons)


"""Identifies the category for building the class object and branching the dialog relating to renting filters"""


@dp.message_handler(lambda message: 'rent' in message.text.lower())    # bot reaction for word 'rent' in message
async def category_identifier(message: types.Message):
    await message.reply("Sure! We'll find a perfect car for You!")
    await bot.send_message(message.from_user.id, "Please, use the menu \U00002B07"
                                                 " to find Your perfect car",
                           reply_markup=kb.category_buttons)
    

"""Economy Section of message and callback handlers"""


@dp.message_handler(lambda message: 'economy' in message.text.lower())
async def economy_category(message: types.Message):
    await message.reply('Economy category\n(15$ - 45$)\n'
                        'Please, use the buttons to navigate \U00002B07',
                        reply_markup=ct_kb.economy_inline_filters_buttons)


@dp.callback_query_handler(text='economy_cars_show')
async def economy_cars_inline(callback: types.CallbackQuery):
    await callback.message.reply(f"Brands in Economy category\U00002B07", reply_markup=brands_bt_generator('economy'))
    
    
@dp.callback_query_handler(Text(startswith='economy_'))
async def economy_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')

    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='ecnm_'))
async def ecnm_model_info(callback: types.CallbackQuery):

    # splits the callback message from inline button to handover the relevant data to the func img_loader and
    # car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=img_loader(brand, car_id),
                         caption=f"{brand} {model}:\n\n{car_info('economy' , brand, model)}",
                         reply_markup=kb.order_bt)
    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""Middle Section of message and callback handlers"""


@dp.message_handler(lambda message: 'middle' in message.text.lower())
async def middle_category(message: types.Message):
    await message.reply('Middle category\n(30$ - 70$)\n'
                        'Please, use the buttons to navigate \U00002B07',
                        reply_markup=ct_kb.middle_inline_filters_buttons)


@dp.callback_query_handler(text='middle_cars_show')
async def middle_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands in Middle category \U00002B07", reply_markup=brands_bt_generator('middle'))


@dp.callback_query_handler(Text(startswith='middle_'))
async def middle_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')
    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='mdl_'))
async def mdl_model_info(callback: types.CallbackQuery):
    # Splits the callback message from inline button to handover the relevant data
    # to the func img_loader and car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(chat_id=callback.message.chat.id, photo=img_loader(brand, car_id), 
                         caption=f"{brand} {model}:\n\n{car_info('middle' , brand, model)}",
                         reply_markup=kb.order_bt)
    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""Business Section of message and callback handlers"""


@dp.message_handler(lambda message: 'business' in message.text.lower())
async def business_category(message: types.Message):
    await message.reply('Business category\n(43$ - 90$)\n'
                        'Please, use the buttons to navigate \U00002B07',
                        reply_markup=ct_kb.business_inline_filters_buttons)


@dp.callback_query_handler(text='business_cars_show')
async def business_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands in Business category \U00002B07", reply_markup=brands_bt_generator('business'))


@dp.callback_query_handler(Text(startswith='business_'))
async def business_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')
    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='bsns_'))
async def bsns_model_info(callback: types.CallbackQuery):
    # splits the callback message from inline button to handover the relevant data
    # to the func img_loader and car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=img_loader(brand, car_id),
                         caption=f"{brand} {model}:\
                                \n\n{car_info('business' , brand, model)}",
                         reply_markup=kb.order_bt)
    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""Premium Section of message and callback handlers"""
                            

@dp.message_handler(lambda message: 'premium' in message.text.lower())
async def premium_category(message: types.Message):
    await message.reply('Premium category\n(Starts from 85$)\n'
                        'Please, use the buttons to navigate \U00002B07',
                        reply_markup=ct_kb.premium_inline_filters_buttons)


@dp.callback_query_handler(text='premium_cars_show')
async def premium_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands in PREMIUM category \U00002B07", reply_markup=brands_bt_generator('premium'))


@dp.callback_query_handler(Text(startswith='premium_'))
async def premium_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')
    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='prem_'))
async def prem_model_info(callback: types.CallbackQuery):
    # splits the callback message from inline button to handover the relevant data
    # to the func img_loader and car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(
                         chat_id=callback.message.chat.id,
                         photo=img_loader(brand, car_id),
                         caption=f"{brand} {model}:\
                         \n\n{car_info('premium', brand, model)}",
                         reply_markup=kb.order_bt
                        )

    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""SUV Section of message and callback handlers"""


@dp.message_handler(lambda message: 'suv' in message.text.lower())
async def suv_category(message: types.Message):
    await message.reply('Suv category\n(Starts from 36$)\n'
                        'Please, use the buttons to navigate \U00002B07', reply_markup=ct_kb.suv_inline_filters_buttons)


@dp.callback_query_handler(text='suv_cars_show')
async def suv_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands in Suv category \U00002B07", reply_markup=brands_bt_generator('suv'))


@dp.callback_query_handler(Text(startswith='suv_'))
async def middle_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')
    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='sv_'))
async def sv_model_info(callback: types.CallbackQuery):
    # splits the callback message from inline button to handover the relevant data
    # to the func img_loader and car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=img_loader(brand, car_id),
                         caption=f"{brand} {model}:\n\n{car_info('suv' , brand, model)}",
                         reply_markup=kb.order_bt)
    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""Minivan Section of message and callback handlers"""
                            

@dp.message_handler(lambda message: 'minivan' in message.text.lower())
async def minivan_category(message: types.Message):
    await message.reply('Minivan category\n(Starts from 33$)\n'
                        'Please, use the buttons to navigate \U00002B07',
                        reply_markup=ct_kb.minivan_inline_filters_buttons)


@dp.callback_query_handler(text='minivan_cars_show')
async def minivan_filters_inline(callback: types.CallbackQuery):
    await callback.message.reply("Brands in Minivan category \U00002B07", reply_markup=brands_bt_generator('minivan'))


@dp.callback_query_handler(Text(startswith='minivan_'))
async def minivan_models_inline(callback: types.CallbackQuery):
    # splits the callback message from inline button in format {category}_{brand}_{model}
    # to handover it to the function mdls_bt_generator which generates the inline buttons
    brand_choosen = callback.data.split('_')
    category = brand_choosen[0]
    brand = brand_choosen[1]
    await callback.message.reply("Models available \U00002B07", reply_markup=mdls_bt_generator(category, brand))


@dp.callback_query_handler(Text(startswith='van_'))
async def van_model_info(callback: types.CallbackQuery):
    # splits the callback message from inline button to handover the relevant data
    # to the func img_loader and car_info as required arguments
    model_choosen = callback.data.split('_')

    brand = model_choosen[1]
    car_id = model_choosen[-1]
    model = model_choosen[2]
    await bot.send_photo(chat_id=callback.message.chat.id,
                         photo=img_loader(brand, car_id),
                         caption=f"{brand} {model}:\n\n{car_info('minivan' , brand, model)}",
                         reply_markup=kb.order_bt)
    img_loader(brand, car_id).seek(0)
    img_loader(brand, car_id).close()


"""Common echo replier"""


@dp.message_handler()
async def echo_reply(message: types.Message):
    await message.reply("Hello! I'm Your assistant. Probably I didn't understand you." 
                        " Please repeat Your question.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


    
