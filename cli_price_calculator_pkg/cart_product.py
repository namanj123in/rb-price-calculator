import sys

'''
Implementation of CartProduct as a representation of a product in a provided
cart JSON consisting of its type, options, markup, and quantity.
'''
class CartProduct:

    def __init__(self, product_type, options, artist_markup, quantity):
        '''
        Initialises below mentioned attributes of a cart product.

        Args:
            product_type (str): type of product, ex. "hoodie"
            options (dict -> str: [str]): ex. "size": ["small", "large"]
            artist_markup (float): percentage increase for artist
            quantity (float): quantity
        Returns:
            None
        '''
        self.__product_type = product_type
        self.__options = options

        try:
            self.__artist_markup = float(artist_markup)
            self.__quantity = float(quantity)
        except ValueError:
            sys.exit("Non-numerical markup and/or quantity values supplied")
