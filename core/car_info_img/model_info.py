import psycopg2
from config import db_pass


def car_info(category: str, brand: str, model: str):
    """
    Function fetches from DB the information regarding particular car specs
    such as : Transmission type, Fuel consumption etc.
    """

    try:
        connect = psycopg2.connect(database='car_rental', user='postgres', password=db_pass)
        curs = connect.cursor()

        # 'suv' and 'minivan' category placed in IF block as they required different query from DB
        if category in ('suv', 'minivan'):

            curs.execute("""SELECT brand, model, price, fuel, motor::float as motor, transmission,
                            air_conditioning, fuel_consumption_100km::float as fuel_consumption_100km, seating_capacity
                            FROM fleet
                            WHERE sub_category = %s and brand = %s and model = %s""", (category, brand, model))
        
            fetched_list = (list(curs.fetchall()[0]))
            titles = [var[0].capitalize() for var in curs.description]
            message = ''
            for (params, header) in zip(fetched_list, titles):
                message += f'{header}:   {params}\n'
            return message
        
        else:

            curs.execute("""SELECT brand, model, price, fuel, motor::float as motor, transmission,
                            air_conditioning, fuel_consumption_100km::float as fuel_consumption_100km, seating_capacity
                            FROM fleet
                            WHERE category = %s and brand = %s and model = %s""", (category, brand, model))

            fetched_list = (list(curs.fetchall()[0]))
            titles = [var[0].capitalize() for var in curs.description]
            message = ''
            for (params, header) in zip(fetched_list, titles):
                message += f'{header}:   {params}\n'
            return message

    finally:
        curs.close()
        connect.close()
    
    
