from config import db_pass
from core.model_list_generator import models_dict_gen
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton



def mdls_bt_generator(category:str,brand:str): 
    """
    Function generates the amount of inline buttons (models in this case) by meaning of fetching the data 
    from dicts generated in dicts_generating func (models_dict_gen()) depends on brand and DB condition
    
    """
    
    final_expression = 'InlineKeyboardMarkup()'
    
    for model in models_dict_gen(category).get(f'{category}_{brand}'): # extracting particular dict from generating func, depending on
                                                                       # func arguments handed over from user request by callback meaning
        if category == 'economy':
            short_category = 'ecnm'
        elif category == 'middle':
            short_category = 'mdl'
        elif category == 'business':
            short_category = 'bsns'
        elif category == 'premium':
            short_category = 'prem'
        elif category == 'suv':
            short_category = 'sv'
        elif category == 'minivan':
            short_category = 'van'
        final_expression += f'.add(InlineKeyboardButton("{model[0]}", callback_data="{short_category}_{brand}_{model[0]}_{model[1]}"))'
    return eval(final_expression)


