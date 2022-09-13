from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton



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

"""Order Section"""
order_bt = InlineKeyboardMarkup().add(InlineKeyboardButton("Order", url="https://support.apple.com/uk-ua/HT204506"))








