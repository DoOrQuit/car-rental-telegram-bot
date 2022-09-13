#from config import img_path
import os


def img_loader(brand:str, car_id:str):
    """Func searches and attaches a car photo user picks"""
    keyword = car_id
    for fname in os.listdir(f'C:/Users/kosan/OneDrive/Documents/Python/Projects/car_rental_telegram_bot/core/car_info_img/img/{brand.lower()}'):
        if keyword in fname:     
            img = open(f'C:/Users/kosan/OneDrive/Documents/Python/Projects/car_rental_telegram_bot/core/car_info_img/img/{brand.lower()}/{fname}/{car_id}.jpg', 'rb')
            return img



