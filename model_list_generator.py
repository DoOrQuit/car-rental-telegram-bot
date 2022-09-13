import psycopg2
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from brand_button_generator import economy_brands_list, middle_brands_list, business_brands_list
from brand_button_generator import premium_brands_list, suv_brands_list, minivan_brands_list





def economy_list_gen():
    """
    Generates the lists of brands in Economy category each of which contains evailable model names
    """
    economy_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand}' 
        #                                                                                      (in this case: economy_{brand})
        for brand in economy_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('economy', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            economy_brands_dict[f"economy_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return economy_brands_dict


def middle_list_gen():
    """
    Generates the lists of brands in Middle category each of which contains evailable model names
    """
    middle_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand}' 
        #                                                                                      (in this case: middle_{brand})
        for brand in middle_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('middle', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            middle_brands_dict[f"middle_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return middle_brands_dict



def business_list_gen():
    """
    Generates the lists of brands in Business category each of which contains evailable model names
    """
    business_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: business_{brand.lower()})
        for brand in business_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('business', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            business_brands_dict[f"business_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return business_brands_dict



def premium_list_gen():
    """
    Generates the lists of brands in Premium category each of which contains evailable model names
    """
    premium_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand}' 
        #                                                                                      (in this case: premium_{brand})
        for brand in premium_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('premium', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            premium_brands_dict[f"premium_{brand}"] = expres

        
    finally:
        curs.close()
        connect.close()

    return premium_brands_dict


def suv_list_gen():
    """
    Generates the lists of brands in Suv category each of which contains evailable model names
    """
    suv_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: suv_{brand.lower()})
        for brand in suv_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE sub_category = %s and brand = %s""", ('suv', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            suv_brands_dict[f"suv_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return suv_brands_dict


def minivan_list_gen():
    """
    Generates the lists of brands in Minivan category each of which contains evailable model names
    """
    minivan_brands_dict = {}
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()
        
        #iteration that creates the lists contains all models available for every single brand with name '{category}_{brand}' 
        #                                                                                      (in this case: minivan_{brand})
        for brand in minivan_brands_list:
            curs.execute("""SELECT DISTINCT model, car_id
                            FROM fleet
                            WHERE sub_category = %s and brand = %s""", ('minivan', f'{brand}'))
            expres = [model for model in curs.fetchall()]
            minivan_brands_dict[f"minivan_{brand}"] = expres
        
    finally:
        curs.close()
        connect.close()

    return minivan_brands_dict
