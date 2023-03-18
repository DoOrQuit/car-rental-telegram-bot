import psycopg2
import asyncio
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""This file contains supportive functions"""


def brands_list_gen(category: str):
    """
    Fetching the list of cars' category to hand over to button generating function
    """
    try:
        connect = psycopg2.connect(database='car_rental',
                                   user='postgres',
                                   password=db_pass)
        curs = connect.cursor()

        # Both categories placed in IF statement due to querying as sub_category
        if category == 'suv' or category == 'minivan':
            curs.execute("""SELECT DISTINCT brand
                            FROM fleet
                            WHERE sub_category = %s """, (category,))
        
            brands_list = [brand[0] for brand in curs.fetchall()]
        
        else:
            curs.execute("""SELECT DISTINCT brand
                            FROM fleet
                            WHERE category = %s """, (category,))
            brands_list = [brand[0] for brand in curs.fetchall()]      

    finally:
        curs.close()
        connect.close()

    return brands_list


def brands_bt_generator(category: str):
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """  
    final_expression = 'InlineKeyboardMarkup()'
    for variable in brands_list_gen(category):
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{category}_{variable}"))'
    return eval(final_expression)
