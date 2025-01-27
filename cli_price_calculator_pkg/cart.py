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
        self.__loaded_cart = self.__load_cart()
        self.__products = self.__load_products()

    def __load_cart(self):
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

    def __load_products(self):
        '''
        Retrieve products from cart JSON and construct corresponding 
        CartProducts(s) returned to and stored by self.__products.
        
        Args:
            (self)
        Returns:
            ([CartProduct]): List of CartProducts from cart JSON.
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

    def get_count(self):
        '''
        Returns the amount of total products in cart.
        
        Args:
            (self)
        Returns:
            (int): Number of stored products in cart.
        '''
        return len(self.__products)

    ##############################  Properties  ################################

    @property
    def products(self):
        '''
        Property-based Getter for products.

        Args:
            (self)
        Returns
            ([CartProduct]): List of CartProduct(s).
        '''
        return self.__products

    @property
    def json_cart(self):
        '''
        Property-based Getter for cart JSON file.

        Args:
            (self)
        Returns
            (str): Cart JSON file.
        '''
        return self.__json_cart

    ##############################  Overridden  ################################

    def __str__(self):
        '''
        String representation (str()) of Cart ->
        -> all products in the cart 
        -> further trigger str() for each product. 

        Args:
            (self)
        Returns
            (str): String representation of all stored products in cart. 
        '''
        return "\n" + "\n".join([str(product) for product in self.__products])
