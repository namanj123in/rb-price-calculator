import sys

class CartProduct:
    '''
    Implementation of CartProduct as a representation of a product in a provided
    cart JSON consisting of its type, options, markup, and quantity.
    -> Check Schema
    '''

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

    #############################   Properties  ################################

    @property
    def product_type(self):
        '''
        Args:
            (self)
        Returns

        '''
        return self.__product_type

    @property
    def options(self):
        return self.__options
    
    @property
    def artist_markup(self):
        return self.__artist_markup

    @property
    def quantity(self):
        return self.__quantity

    #############################   Overridden  ################################
    
    def __str__(self):
        option_types = sorted(self.__options.keys())
        return f"\nType: {self.__product_type}\nOptions: {option_types}\n" + \
                f"Markup: {self.__artist_markup}\nQuantity: {self.__quantity}\n"

