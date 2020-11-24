'''
test_cart.py
To run: `python -m unittest tests.test_cart -v`(from top-level folder)

More information in README.
'''
import os
import json
import unittest
from os.path import join
from cli_price_calculator_pkg.cart import Cart

class TestCart(unittest.TestCase):
    '''
    Testing file for class Cart in main package cli_price_calculator_pkg.

    (The tests are conducted for sample test cart files stored in fixtures.)
    '''
    @classmethod
    def setUpClass(self):
        '''
        Runs once when TestCart is called. 
        
        Sets absolute path to tests\fixtures.

        Args:
            (self)
        Returns:
            None.
        '''
        self.abs_path = join(os.getcwd(), "tests", "fixtures")

    @classmethod
    def tearDownClass(self):
        '''
        Runs at the end of the TestCart call to perform clean-up duties. No
        real purpose at the moment as no side-effects take place but might need
        in the future.
        '''
        pass

    ################################  TESTS  ##################################

    def test_normal_cart_counts(self):
        '''
        Tests for the quantity of items stored in 'normal' Cart(s) - originally supplied.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        # Read normal test cart files from FILES.json in \fixtures
        with open(os.path.join(self.abs_path, "NORMAL_FILES.json"), "r") as f:
            normal_cart_files = json.load(f)["cart_files"]

        for cart_file in normal_cart_files:
            expected = f"{cart_file}-expected.json"
            cart_file = f"{cart_file}.json"
        
            self.counts_test_runner(cart_file, expected)

    def test_normal_cart_content(self):
        '''
        Tests for the content of items stored in 'normal' Cart(s) - originally supplied.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        # Read normal test cart files from FILES.json in \fixtures
        with open(os.path.join(self.abs_path, "NORMAL_FILES.json"), "r") as f:
            normal_cart_files = json.load(f)["cart_files"]

        for cart_file in normal_cart_files:
            expected = f"{cart_file}-expected.json"
            cart_file = f"{cart_file}.json"
        
            self.content_test_runner(cart_file, expected)

    def test_empty_cart_count(self):
        '''
        Tests for cart count of an empty cart.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.counts_test_runner("cart-0-empty.json",
                                "cart-0-empty-expected.json"
                                )

    def test_empty_cart_content(self):
        '''
        Tests for cart contents of an empty cart.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.content_test_runner("cart-0-empty.json",
                                 "cart-0-empty-expected.json"
                                )

    def counts_test_runner(self, cart, expected):
        '''
        A general test runner for cart count and content tests. 
        Checks if the cart content and quantity is correct.

        Uses expected data files with suffix "-expected" in \fixtures 
        to determine correct values(s) from key 'count'. 

        Args:
            cart (str): JSON file of test cart.
            expected (str): JSON file of expected test cart file.
        Returns:
            None.
        Raises:
            AssertionError
        '''
        test_cart = join(self.abs_path, cart)
        expected = join(self.abs_path, expected)

        with open(expected, "r") as f:
            expected_json = json.load(f)

        cart = Cart(test_cart)
        self.assertEqual(cart.get_count(), expected_json["count"])

    def content_test_runner(self, cart, expected):
        '''
        A general test runner for cart content tests. 
        Checks if the cart content is correct based on cart's __str__ representation.

        Uses expected data files with suffix "-expected" in \fixtures 
        to determine correct values(s) from key 'cart_str'. 

        Args:
            cart (str): JSON file of test cart.
            expected (str): JSON file of expected test cart file.
        Returns:
            None.
        Raises:
            AssertionError
        '''
        test_cart = join(self.abs_path, cart)
        expected = join(self.abs_path, expected)

        with open(expected, "r") as f:
            expected_json = json.load(f)

        cart = Cart(test_cart)
        self.assertEqual(str(cart).strip(), expected_json["cart_str"])

    



    


