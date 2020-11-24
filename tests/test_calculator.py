'''
test_calculator.py
To run: `python -m unittest tests.test_calculator -v`(from top-level folder)

More information in README.
'''
import unittest
import json
import os
from os.path import join
from cli_price_calculator_pkg.cart import Cart
from cli_price_calculator_pkg.product_data import BaseProductData
from cli_price_calculator_pkg.cli_price_calculator import CLIPriceCalculator

class TestCalculator(unittest.TestCase):
    '''
    Testing file for class CLIPriceCalculator in main package 
    cli_price_calculator_pkg.

    (The tests are conducted for sample test cart and base-price files stored 
    in fixtures.)
    '''
    @classmethod
    def setUpClass(self):
        '''
        Runs once when TestCalculator is called. 
        
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

    def test_normal_totals(self):
        '''
        Tests for the total calculated values of 'normal' Cart(s) - originally supplied. 

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        # Read relevant test cart and base-price files from FILES.json in 
        # \fixtures
        with open(os.path.join(self.abs_path, "NORMAL_FILES.json"), "r") as f:
            normal_cart_files = json.load(f)["cart_files"]

        for cart_file in normal_cart_files:
            expected = f"{cart_file}-expected.json"

            # Cart files and corresponding base-price files have the same suffix
            suffix = cart_file.split("-")[-1]
            base_prices = f"base-prices-{suffix}.json"
            cart_file = f"{cart_file}.json"

            self.general_test_runner(cart_file, expected, base_prices)
            
    def test_total_extra_option(self):
        '''
        Tests for calculated value of base-file with additional option of 'gender'.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.general_test_runner("cart-11986-custom_option.json",
                                 "cart-11986-custom_option-expected.json",
                                 "base-prices-custom_option.json")

    def test_total_empty_cart(self):
        '''
        Tests for calculated value of empty cart.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.general_test_runner("cart-0-empty.json",
                                 "cart-0-empty-expected.json",
                                 "base-prices-normal.json"
                                )

    def test_total_repeated_cart_product(self):
        '''
        Tests for calculated value of cart with two products with different
        quantities.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.general_test_runner("cart-repeated_cart_value.json",
                                 "cart-repeated_cart_value-expected.json",
                                 "base-prices-custom_option.json"
                                )

    def general_test_runner(self, cart, expected, prices):
        '''
        A general test runner for total_price tests. Checks if the calculated
        total price of inoput cart is correct given cart, expected JSON, and 
        base-prices.

        Args:
            cart (str): JSON file of test cart.
            expected (str): JSON file of expected test cart file.
            prices (str): JSON file of base_prices file.
        Returns:
            None.
        Raises:
            AssertionError
        '''
        test_cart = join(self.abs_path, cart)
        expected = join(self.abs_path, expected)
        test_prices = join(self.abs_path, prices)

        cart = Cart(test_cart)
        base_prices = BaseProductData(test_prices)
        calculator = CLIPriceCalculator(cart, base_prices)

        with open(expected, "r") as f:
            expected_total = json.load(f)["total_price"]

        self.assertEqual(calculator.cart_total, expected_total)
