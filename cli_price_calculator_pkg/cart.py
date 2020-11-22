'''
cart.py
'''
import json
import sys
from cli_price_calculator_pkg.cart_product import CartProduct

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
        self.__products = self.load_products()

    def load_cart(self):
        '''
        Loads cart JSON returned to and stored by self.__loaded_cart.

        -> Can cause early exit, if unable to load JSON file.

        Args:
            (self)
        Returns:
            (dict): JSON data from cart JSON.
        '''
        try:
            with open(self.__json_cart, "r") as cart_f:
                cart_data = json.load(cart_f)
        except:
            sys.exit(f"Something went wrong! Could not load {self.__json_cart}")
        return cart_data

    def load_products(self):
         '''
        Retrieve products from cart JSON and construct corresponding 
        CartProducts(s) returned to and stored by self.__products.
        
        Args:
            (self)
        Returns:
            [CartProduct]: List of CartProducts from cart JSON.
        '''
        products = []
        for product in self.__loaded_cart:
            product_type = product["product-type"]
            options = product["options"]
            markup = product["artist-markup"]
            quantity= product["quantity"]

            cart_product = CartProduct(product_type, options, markup, quantity)
            products.append(cart_product)

        return products
