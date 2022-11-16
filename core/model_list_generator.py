import psycopg2
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.brand_button_generator import brands_list_gen


def models_dict_gen(category: str) -> dict:
    """
    Generates the dicts of brands in category (specified as argument) each of which contains available model names
    """
    models_dict = {}
    try:
        connect = psycopg2.connect(database='car_rental', user='postgres', password=db_pass)
        curs = connect.cursor()

        # iteration that creates the lists contains
        # all models available for every single brand
        if category == 'suv' or category == 'minivan':

            for brand in brands_list_gen(category):

                curs.execute("""SELECT DISTINCT model, car_id
                                FROM fleet
                                WHERE sub_category = %s and brand = %s""", (category, brand))
                expres = [model for model in curs.fetchall()]
                models_dict[f"{category}_{brand}"] = expres
        else:

            for brand in brands_list_gen(category):

                curs.execute("""SELECT DISTINCT model, car_id
                                FROM fleet
                                WHERE category = %s and brand = %s""", (category, brand))
                expres = [model for model in curs.fetchall()]
                models_dict[f"{category}_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return models_dict
