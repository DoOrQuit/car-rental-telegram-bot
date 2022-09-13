#from config import db_pass
from model_list_generator import economy_list_gen, middle_list_gen, business_list_gen, premium_list_gen, suv_list_gen, minivan_list_gen
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton



def economy_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in economy_list_gen().get(f'economy_{brand}'):  # here were lowered string
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="ecnm_{brand}_{model}"))' # here were lowered string
    return eval(final_expression)


def middle_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    for model in middle_list_gen().get(f'middle_{brand}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="mdl_{brand}_{model}"))'
    return eval(final_expression)


def business_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    for model in business_list_gen().get(f'business_{brand}'):  
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="bsns_{brand}_{model}"))'
    return eval(final_expression)


def premium_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in premium_list_gen().get(f'premium_{brand}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="prem_{brand}_{model}"))'
    return eval(final_expression)


def suv_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in suv_list_gen().get(f'suv_{brand}'): 
        final_expression += f'.add(InlineKeyboardButton("{model}", callback_data="sv_{brand}_{model}"))'
    return eval(final_expression)


def minivan_mdls_bt_generator(brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in minivan_list_gen().get(f'minivan_{brand}'):
        final_expression += f'.add(InlineKeyboardButton("{model[0]}", callback_data="van_{brand}_{model[0]}_{model[1]}"))'
    return eval(final_expression)



