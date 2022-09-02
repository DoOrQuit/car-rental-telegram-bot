import psycopg2
import pprint


def car_info(category:str, brand:str, model:str):
    if category == 'ecnm':
        category = 'economy'
    else:
        pass
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        curs.execute("""SELECT brand, model, price, fuel, motor::float as motor, transmission,
                             air_conditioning, fuel_consumption_100km::float as fuel_consumption_100km, seating_capacity
                        FROM fleet
                        WHERE category = %s and brand = %s and model = %s""", (category, brand.capitalize(), model.capitalize()))
    
        fetched_list = (list(curs.fetchall()[0]))
        header = [var[0].capitalize() for var in curs.description]
        car_info = dict(zip(header, fetched_list))
        result = pprint.pformat(car_info, width=1, sort_dicts=False)
    except:
        print('oops. DB die')
    finally:
        curs.close()
        connect.close()
    return result
    
