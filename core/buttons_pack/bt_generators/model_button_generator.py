import psycopg2
#from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from core.buttons_pack.bt_generators.model_list_generator import * 





def economy_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'economy_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="ecnm_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)


def middle_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'middle_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="mdl_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)


def business_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'business_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="bsns_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)


def premium_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'premium_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="prem_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)


def suv_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'suv_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="sv_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)


def minivan_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in eval(f'minivan_{brand.lower()}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="van_{brand.lower()}_{model.lower()}"))'
    return eval(final_expression)



