import psycopg2
from config import db_pass
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


# Fetching the list of VW models in economy categories to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = db_pass)
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = %s and brand = %s""", ('economy', 'vw' ))
   
    economy_brands_list = [model[0] for model in curs.fetchall()]

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
