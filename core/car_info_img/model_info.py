import psycopg2
import pprint


def car_info(category:str , model:str):
    
    try:
        connect = psycopg2.connect(database = 'car_rental', 
                                    user = 'postgres', 
                                    password = 'datapass')
        curs = connect.cursor()
        curs.execute("""SELECT *
                        FROM fleet
                        WHERE category = %s and model = %s""", (category, model.capitalize()))
    
        fetched_list = (list(curs.fetchall()[0]))[2:]
        header = [var[0].capitalize() for var in curs.description]
        car_info = dict(zip(header[2:], fetched_list))
        pprint.pprint(car_info, width=1)
    except:
        print('oops. DB die')
    finally:
        curs.close()
        connect.close()
