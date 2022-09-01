import psycopg2
#from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from core.buttons_pack.bt_generators.model_list_generator import * 





def model_bt_generator(): 
    """
    Function generates the amount of inline buttons (models in this case) depends on brand and DB condition
    
    """
    final_expression = 'InlineKeyboardMarkup()'
    for variable in economy_vw:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="economy_{variable.lower()}"))'
    return eval(final_expression)