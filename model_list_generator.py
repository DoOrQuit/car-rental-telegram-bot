import psycopg2
#from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from brand_button_generator import economy_brands_list, middle_brands_list, business_brands_list
from brand_button_generator import premium_brands_list, suv_brands_list, minivan_brands_list




"""Generates the lists of brands in Economy category each of which contains evailable model names"""
def economy_list_gen():    
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: economy_{brand.lower()})
        temp_var = ''
        for brand in economy_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('economy', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"economy_{brand.lower()} = {expres}\n"
            exec(temp_var)
        
    finally:
        curs.close()
        connect.close()
   


"""Generates the lists of brands in Middle category each of which contains evailable model names"""
def middle_list_gen():
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: middle_{brand.lower()})
        temp_var = ''
        for brand in middle_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('middle', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"middle_{brand.lower()} = {expres}\n"
            

    finally:
        curs.close()
        connect.close()


"""Generates the lists of brands in Business category each of which contains evailable model names"""
def business_list_gen():
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: business_{brand.lower()})
        temp_var = ''
        for brand in business_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('business', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"business_{brand.lower()} = {expres}\n"
            exec(temp_var)

    finally:
        curs.close()
        connect.close()


"""Generates the lists of brands in Premium category each of which contains evailable model names"""
def premium_list_gen():
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: premium_{brand.lower()})
        temp_var = ''
        for brand in premium_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('premium', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"premium_{brand.lower()} = {expres}\n"
            exec(temp_var)

    finally:
        curs.close()
        connect.close()


"""Generates the lists of brands in Suv category each of which contains evailable model names"""
def suv_list_gen():
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: suv_{brand.lower()})
        temp_var = ''
        for brand in suv_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('suv', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"suv_{brand.lower()} = {expres}\n"
            exec(temp_var)

    finally:
        curs.close()
        connect.close()


"""Generates the lists of brands in Minivan category each of which contains evailable model names"""
def minivan_list_gen():
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        
        #iteration that creates the list contains all models available for every single brand with name '{category}_{brand.lower()}' 
        #                                                                                      (in this case: minivan_{brand.lower()})
        temp_var = ''
        for brand in minivan_brands_list:
            curs.execute("""SELECT DISTINCT model
                            FROM fleet
                            WHERE category = %s and brand = %s""", ('minivan', f'{brand}'))
            expres = [x[0] for x in curs.fetchall()] 
            temp_var+=f"minivan_{brand.lower()} = {expres}\n"
            exec(temp_var)

    finally:
        curs.close()
        connect.close()

if __name__ == '__main__':
    print(economy_brands_list)