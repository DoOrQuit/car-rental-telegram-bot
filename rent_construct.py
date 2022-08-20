import asyncio
import psycopg2
from config import db_pass
#from main import category_identifier

#class car_order():
    #"""Class that difines car choosen by price or category, brand"""
    #def __init__(self,  nominal_price : int, category = category_identifier(), brand = None):
        #self.nominal_price = nominal_price
        #self.category = category
        #self.brand = brand

try:
    conn = psycopg2.connect(database = 'car_rental', 
                            user = 'postgres', 
                            password = db_pass)
    curs = conn.cursor()
        
    curs.execute("""SELECT brand, model, fuel, price
                    FROM fleet
                    WHERE category = %s""", ('economy',))
    fetch = curs.fetchall()
    
    for row in fetch:
        print(row)  
finally:
    curs.close()
    conn.close()



        