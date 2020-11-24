'''
test_product_data.py
To run: `python -m unittest tests.test_product_data -v`(from top-level folder)

More information in README.
'''
import unittest
import json
import os
from os.path import join
from cli_price_calculator_pkg.exceptions import SchemaException
from cli_price_calculator_pkg.cart import Cart
from cli_price_calculator_pkg.product_data import BaseProductData

class TestProductData(unittest.TestCase):
    '''
    Testing file for class BaseProductData in main package 
    cli_price_calculator_pkg.

    (The tests are conducted for sample test cart and base-price files stored 
    in fixtures.)
    '''
    @classmethod
    def setUpClass(self):
        '''
        Runs once when TestProductData is called. 
        
        Sets absolute path to tests\fixtures.

        Args:
            (self)
        Returns:
            None.
        '''
        # Absolute path to \fixtures
        self.abs_path = join(os.getcwd(), "tests", "fixtures")

    @classmethod
    def tearDownClass(self):
        '''
        Runs at the end of the TestCart call to perform clean-up duties. No
        real purpose at the moment as no side-effects take place but might need
        in the future.
        '''
        pass

    def test_base_value_retrieval(self):
        '''
        Tests for base prices retrieved via. price_tree from BaseProductData.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        cart_file = join(self.abs_path, "cart-base-values-custom_option.json")
        test_prices = join(self.abs_path, "base-prices-custom_option.json")
        # 3 products in cart file
        expected_prices = [3500, 583, 5000]

        cart = Cart(cart_file)
        base_prices = BaseProductData(test_prices)
        actual_prices = [base_prices.cart_product_base_price(product)  \
                            for product in cart.products]

        self.assertEqual(actual_prices, expected_prices)

    def test_repeated_base_val_exception(self):
        '''
        Tests if SchemaException is raised when a product is encountered in base-prices with different original prices.

        Args:
            (self)
        Returns:
            None.
        '''
        base_prices = join(self.abs_path, "base-prices-repeated_val.json")
        with self.assertRaises(SchemaException):
            BaseProductData(base_prices)
