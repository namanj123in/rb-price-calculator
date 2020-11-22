'''
cart_product_.py
'''
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
            product_type (str): Type of product, ex. "hoodie"
            options (dict -> str: [str]): ex. "size": ["small", "large"]
            artist_markup (float): Percentage increase for artist
            quantity (float): Quantity
        Returns:
            None.
        '''
        self.__product_type = product_type
        self.__options = options

        try:
            self.__artist_markup = float(artist_markup)
            self.__quantity = float(quantity)
        except ValueError:
            sys.exit("Non-numerical markup and/or quantity values supplied")

    ##############################  Properties  ################################

    @property
    def product_type(self):
        '''
        Property-based Getter for product_type.

        Args:
            (self)
        Returns
            (str): Product-type of (self) product.
        '''
        return self.__product_type

    @property
    def options(self):
        '''
        Property-based Getter for options.

        Args:
            (self)
        Returns
            (dict -> str: [str]): option-type -> options.
        '''
        return self.__options
    
    @property
    def artist_markup(self):
        '''
        Property-based Getter for artist-markup.

        Args:
            (self)
        Returns
            (float): Percentage increase for artist. 
        '''
        return self.__artist_markup

    @property
    def quantity(self):
        '''
        Property-based Getter for quantity.

        Args:
            (self)
        Returns
            (float): Product quantity. 
        '''
        return self.__quantity

    ##############################  Overridden  ################################
    
    def __str__(self):
        '''
        String representation (str()) of CartProduct -> a concatenation of 
        provided attributes.

        Args:
            (self)
        Returns
            (str): product-type of (self) product 
        '''
        option_types = sorted(self.__options.keys())
        return f"\nType: {self.__product_type}\nOptions: {option_types}\n" + \
                f"Markup: {self.__artist_markup}\nQuantity: {self.__quantity}\n"

