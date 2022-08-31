from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from core.buttons_pack.bt_generators.brand_button_generator import economy_bt_generator, middle_bt_generator, business_bt_generator
from core.buttons_pack.bt_generators.brand_button_generator import premium_bt_generator, suv_bt_generator, minivan_bt_generator



"""Economy Main menu"""
economy_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='economy_cars_show') #Shows the brands in owner's fleet 
economy_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='economy_price_filter') #Shows the cars in particular price category

economy_inline_filters_buttons = InlineKeyboardMarkup().row(economy_cars_inline_bt, economy_byprice_inline_bt)
"""Economy Secondary menu"""
economy_brands_inline = economy_bt_generator()


"""Middle category filters"""
middle_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='middle_cars_show') #Shows the brands in owner's fleet 
middle_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='middle_price_filter') #Shows the cars in particular price category

middle_inline_filters_buttons = InlineKeyboardMarkup().row(middle_cars_inline_bt, middle_byprice_inline_bt)
"""Middle Secondary menu"""
middle_brands_inline = middle_bt_generator()


"""Business category filters"""
business_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='business_cars_show') #Shows the brands in owner's fleet 
business_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='business_price_filter') #Shows the cars in particular price category

business_inline_filters_buttons = InlineKeyboardMarkup().row(business_cars_inline_bt, business_byprice_inline_bt)
"""Business Secondary menu"""
business_brands_inline = business_bt_generator()


"""Premium category filters"""
premium_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='premium_cars_show') #Shows the brands in owner's fleet 
premium_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='premium_price_filter') #Shows the cars in particular price category

premium_inline_filters_buttons = InlineKeyboardMarkup().row(premium_cars_inline_bt, premium_byprice_inline_bt)
"""Premium Secondary menu"""
premium_brands_inline = premium_bt_generator()


"""SUV category filters"""
suv_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='suv_cars_show') #Shows the brands in owner's fleet 
suv_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='suv_price_filter') #Shows the cars in particular price category

suv_inline_filters_buttons = InlineKeyboardMarkup().row(suv_cars_inline_bt, suv_byprice_inline_bt)
"""Suv Secondary menu"""
suv_brands_inline = suv_bt_generator()


"""Minivan category filters"""
minivan_cars_inline_bt = InlineKeyboardButton("All Cars", callback_data='minivan_cars_show') #Shows the brands in owner's fleet 
minivan_byprice_inline_bt = InlineKeyboardButton('Filter by Price', callback_data='minivan_price_filter') #Shows the cars in particular price category

minivan_inline_filters_buttons = InlineKeyboardMarkup().row(minivan_cars_inline_bt, minivan_byprice_inline_bt)
"""Minivan Secondary menu"""
minivan_brands_inline = minivan_bt_generator()