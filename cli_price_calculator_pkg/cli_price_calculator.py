'''
cli_price_calculator.py
'''
from cli_price_calculator_pkg.exceptions import SchemaException
import sys

class CLIPriceCalculator:
    '''
    Implementation of CLIPriceCalculator as the central class to drive workflow
    from products in the Cart to calculating their totals via. BaseProductData.
    '''
    def __init__(self, cart, prices):
        '''
        Use the provided cart and base-prices to calculate the total value
        of the cart.

        Args:
            cart (Cart): The Cart to calculate the total of.
            prices (BaseProductData): Database of base-prices -> price_tree
        Returns:
            None.
        '''
        self.__cart = cart
        self.__prices = prices
        self.__cart_total = self.calculate_cart_total_cents()
        
    def calculate_cart_total_cents(self):
        '''
        Return the total cart price. Iterate through all products in the
        Cart, retrieve base-price, and calculate the product total. Add all
        product totals.

        Might exit early in case the SchemaException is encountered.

        Args:
            (self) 
        Returns:
            (int): The total value of products in cart.
        '''
        cart_total = 0

        for product in self.__cart.products:
            artist_markup = product.artist_markup
            quantity = product.quantity

            # Retrieve base-price of product from ProductData 
            try:
                base_price = self.__prices.cart_product_base_price(product)
            except SchemaException as error:
                sys.exit(error.message)

            product_total = (base_price +   \
                            round(base_price * (artist_markup / 100))) *  \
                            quantity

            cart_total += product_total

        return cart_total

    ##############################  Properties  ################################

    @property
    def cart_total(self):
        '''
        Property-based Getter for cart_total.

        Args:
            (self)
        Returns
            (int): the total for the (self) cart.
        '''
        return self.__cart_total
    
