import psycopg2
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton





def model_bt_generator(category : str): 
    """
    Function generates the amount of inline buttons (models in this case)  depends on brand and DB condition
    
    """  
    final_expression = 'InlineKeyboardMarkup()'
    for variable in category:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_{category}"))'
    return eval(final_expression)