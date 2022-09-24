import psycopg2
import pprint
from config import db_pass


def car_info(category:str, brand:str, model:str):
    """
    Function fetches from DB the information regarding particular car specs such as : Transmission type, Fuel consumption etc.
    """

    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = db_pass)
        curs = connect.cursor()

        if category in ('suv', 'minivan'):  # 'suv' and 'minivan' category placed in IF block as they required different query from DB
            
            curs.execute("""SELECT brand, model, price, fuel, motor::float as motor, transmission,
                            air_conditioning, fuel_consumption_100km::float as fuel_consumption_100km, seating_capacity
                            FROM fleet
                            WHERE sub_category = %s and brand = %s and model = %s""", (category, brand, model))
        
            fetched_list = (list(curs.fetchall()[0]))
            header = [var[0].capitalize() for var in curs.description]
            car_info = dict(zip(header, fetched_list))  # pprint is used to bring the car information to the client side as 
                                                        # readible message in Telegram chat
            result = pprint.pformat(car_info, width=1, sort_dicts=False)
            return result
        
        else:

            curs.execute("""SELECT brand, model, price, fuel, motor::float as motor, transmission,
                            air_conditioning, fuel_consumption_100km::float as fuel_consumption_100km, seating_capacity
                            FROM fleet
                            WHERE category = %s and brand = %s and model = %s""", (category, brand, model))

            fetched_list = (list(curs.fetchall()[0]))
            header = [var[0].capitalize() for var in curs.description]
            car_information = dict(zip(header, fetched_list))
            result = pprint.pformat(car_information, width=1, sort_dicts=False)
            return result

    except:
        print('oops. DB die')
    finally:
        curs.close()
        connect.close()
    
    
