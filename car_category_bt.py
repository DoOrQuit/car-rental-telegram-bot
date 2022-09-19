from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from brand_button_generator import brands_bt_generator



"""Economy Main menu"""
economy_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='economy_cars_show') #Shows the brands in owner's fleet 
economy_inline_filters_buttons = InlineKeyboardMarkup().row(economy_cars_inline_bt)


"""Middle category filters"""
middle_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='middle_cars_show') #Shows the brands in owner's fleet 
middle_inline_filters_buttons = InlineKeyboardMarkup().row(middle_cars_inline_bt)


"""Business category filters"""
business_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='business_cars_show') #Shows the brands in owner's fleet 
business_inline_filters_buttons = InlineKeyboardMarkup().row(business_cars_inline_bt)


"""Premium category filters"""
premium_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='premium_cars_show') #Shows the brands in owner's fleet 
premium_inline_filters_buttons = InlineKeyboardMarkup().row(premium_cars_inline_bt)


"""SUV category filters"""
suv_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='suv_cars_show') #Shows the brands in owner's fleet 
suv_inline_filters_buttons = InlineKeyboardMarkup().row(suv_cars_inline_bt)


"""Minivan category filters"""
minivan_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='minivan_cars_show') #Shows the brands in owner's fleet 
minivan_inline_filters_buttons = InlineKeyboardMarkup().row(minivan_cars_inline_bt)


