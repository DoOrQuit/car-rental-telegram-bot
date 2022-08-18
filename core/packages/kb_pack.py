from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

start_button = KeyboardButton('/start')
help_button = KeyboardButton('/help')
contacts_button = KeyboardButton('/contacts')

main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

main_buttons.add(start_button).add(help_button).add(contacts_button)


