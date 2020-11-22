'''
cart.py
'''
import json
import sys

class Cart:
    '''
    Implementation of Cart as a representation of a Redbubble Cart.
    - Loads data from provided cart JSON.
    - Constructs CartProduct(s) from loaded data and stores them for later 
      recall.
    '''
    def __init__(self, json_cart):
        '''
        Constructor for Cart - intialise cart JSON.
        
        Args:
            (str): Path to the cart JSON.
        Returns:
            None.
        '''
        self.__json_cart = json_cart
        self.__loaded_cart = self.load_cart()

    def load_cart(self):
        # Load cart data
        try:
            with open(self.__json_cart, "r") as cart_f:
                cart_data = json.load(cart_f)
        except:
            sys.exit(f"Something went wrong! Could not load {self.__json_cart}")
        return cart_data
