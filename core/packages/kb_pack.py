from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import psycopg2
from utilities import economy_bt_generator

"""Main buttons"""
start_bt = KeyboardButton('/start')
help_bt = KeyboardButton('/help')
contacts_bt = KeyboardButton('/contacts')
car_rent_bt = KeyboardButton('Rent \U0001F698')

main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_buttons.add(car_rent_bt).add(help_bt).add(contacts_bt)


"""Help Buttons / Main"""
share_phone = KeyboardButton("Call me Back \U0001F4DE", request_contact=True)
assistant_contact = KeyboardButton("Get an assistant number \U0001F4DE")

help_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_buttons.row(share_phone, assistant_contact)


"""Rent. Category Buttons"""
economy_bt = KeyboardButton('Economy')
middle_bt=KeyboardButton('Middle')
business_bt = KeyboardButton('Business')
premium_bt = KeyboardButton('PREMIUM')
suv_bt = KeyboardButton('Suv')
minivan_bt = KeyboardButton('Minivan')

category_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
category_buttons.row(economy_bt, middle_bt, business_bt)
category_buttons.row(premium_bt)
category_buttons.row(suv_bt, minivan_bt)

"""Economy Main menu"""

economy_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='economy_cars_show') #Shows the brands in owner's fleet 
economy_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='economy_price_filter') #Shows the cars in particular price category

economy_inline_filters_buttons = InlineKeyboardMarkup().row(economy_cars_inline_bt, economy_byprice_inline_bt)
"""Economy Secondary menu"""

economy_brands_inline = economy_bt_generator()





"""Middle category filters"""

"""Business category filters"""

"""Premium category filters"""

"""SUV category filters"""

"""Minivan category filters"""




