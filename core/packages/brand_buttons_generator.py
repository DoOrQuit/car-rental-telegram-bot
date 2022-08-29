import psycopg2
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton



"""This file contains supportive functions"""


# Fetching the list of economy cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = 'economy'""")
   
    economy_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def economy_bt_generator(): 
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """  
    final_expression = 'InlineKeyboardMarkup()'
    for variable in economy_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_economy"))'
    return eval(final_expression)


# Fetching the list of middle cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = 'middle'""")
   
    middle_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def middle_bt_generator():
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """   
    final_expression = 'InlineKeyboardMarkup()'
    for variable in middle_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_middle"))'
    return eval(final_expression)


# Fetching the list of business cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = 'business'""")
   
    business_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def business_bt_generator():
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """   
    final_expression = 'InlineKeyboardMarkup()'
    for variable in business_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_business"))'
    return eval(final_expression)

# Fetching the list of premium cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = 'premium'""")
   
    premium_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def premium_bt_generator():
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """  
    final_expression = 'InlineKeyboardMarkup()'
    for variable in premium_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_premium"))'
    return eval(final_expression)

# Fetching the list of suv cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE sub_category = 'suv'""")
   
    suv_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def suv_bt_generator():
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """   
    final_expression = 'InlineKeyboardMarkup()'
    for variable in suv_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_suv"))'
    return eval(final_expression)

# Fetching the list of minivan cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE sub_category = 'minivan'""")
   
    minivan_brands_list = [brand[0] for brand in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def minivan_bt_generator():
    """
    Function generates the amount of inline buttons (brands in this case) depends on DB condition
    
    """  
    final_expression = 'InlineKeyboardMarkup()'
    for variable in minivan_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}_minivan"))'
    return eval(final_expression)