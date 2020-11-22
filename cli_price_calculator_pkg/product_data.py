'''
product_data.py
'''
import json
import sys

class BaseProductData:
    '''
    Implementation of BaseProductData as a representation of a Redbubble 
    base-prices database.
    - Loads data from provided base-prices JSON.
    '''

    def __init__(self, json_prices):
        self.__json_prices = json_prices
        self.__loaded_prices = self.load_prices()
        self.__count = 0

        self.__price_tree, self.__relevant_options = self.generate_price_tree()

    def load_prices(self):
        '''
        Loads base-prices JSON returned to and stored by self.__loaded_prices.

        -> Can cause early exit, if unable to load JSON file.

        Args:
            (self)
        Returns:
            (dict): JSON data from base-prices JSON.
        '''
        try:
            with open(self.__json_prices, "r") as prices_f:
                prices_data = json.load(prices_f)
        except:
            sys.exit(f"Something went wrong! Could not load {self.__json_prices}")
        return prices_data

