import asyncio
from main import category_identifier

class car_order():
    """Class that difines car choosen by price or category, brand"""
    def __init__(self,  nominal_price : int, category = category_identifier(), brand = None):
        self.nominal_price = nominal_price
        self.category = category
        self.brand = brand
    

        