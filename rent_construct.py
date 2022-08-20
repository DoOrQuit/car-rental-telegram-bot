import asyncio
from car_rental_telegram_bot.main import category_identifier
import main

class car_order():
    """Class that difines car choosen by price or category, brand"""
    def __init__(self,  nominal_price : str, category = None, brand = None):
        self.nominal_price = nominal_price
        self.category = category_identifier()
        self.brand = brand
    

        