import psycopg2



"""This file contains supportive functions"""


# Fetching the list of economy cars category to hand over to button generating function
try:
    connect = psycopg2.connect(database = 'car_rental', 
                        user = 'postgres', 
                        password = 'datapass')
    curs = connect.cursor()
    curs.execute("""SELECT DISTINCT brand
                    FROM fleet
                    WHERE category = 'economy'""")
   
    economy_brands_list = [x[0] for x in curs.fetchall()]

except:
    print('oops. DB die')
finally:
    curs.close()
    connect.close()

def economy_bt_generator(): # Function generates the quantity of inline buttons (brands in this case) depends on DB condition   
    final_expression = 'InlineKeyboardMarkup()'
    for variable in economy_brands_list:
        final_expression += f'.add(InlineKeyboardButton("{variable}", callback_data="{variable.lower()}"))'
    return eval(final_expression)