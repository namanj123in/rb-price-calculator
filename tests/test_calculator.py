'''
test_cart.py
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
    Testing file for class CLIPriceCalculator in main 
    package cli_price_calculator_pkg.

    - Tests the calculated totals.

    (The tests are conducted for sample test cart and base-price files stored 
    in fixtures.)
    '''

    @classmethod
    def setUpClass(self):
        '''
        Sets up the fixtures of test files and expected-result files to be 
        used for the following tests.

        Runs once when TestCalculator is called.

        Args:
            (self)
        Returns:
            None.
        '''
        # Absolute path to \fixtures
        abs_path = join(os.getcwd(), "tests", "fixtures")

        # Read relevant test cart and base-price files from FILES.json in 
        # \fixtures
        with open(os.path.join(abs_path, "FILES.json"), "r") as f:
            loaded_json = json.load(f)
            cart_files = loaded_json["cart_files"]
            base_files = loaded_json["base_files"]

        # For cart and expected test files, append path to ..\fixtures
        # to construct complete absolute paths to test files
        abs_cart_files = []
        expected_files = []
        for file in cart_files:
            abs_cart_files.append(f"{join(abs_path, file)}.json")

            # For each cart file, the corresponding 'expected' data file is 
            # identified by the suffix '-expected' 
            expected_files.append(f"{join(abs_path, file)}-expected.json")

        base_files = [f"{join(abs_path, file)}.json" for file in base_files]

        self.__carts = {}
        self.__base_prices = {}

        # Associate each file with corresponding expected-result file
        self.__expected = dict(zip (abs_cart_files, expected_files))

        TestCalculator.load_test_files(abs_cart_files, base_files)
    
    @classmethod
    def load_test_files(self, cart_files, base_files):
        '''
        Converts each cart file in cart_files to corresponding Cart object,
        and stores in self.__cart. Also, replaces expected_files from files
        to corresponding JSON objects.

        Args:
            ([str]): List of absolute path cart JSON files
        Returns:
            None. 
        '''
        for file in cart_files:
            self.__carts[file] = Cart(file)

        # Replace expected_file(s) to corresponding JSON objects
        for cart_file, expected_file in self.__expected.items():
            with open(expected_file, "r") as expected_f:
                self.__expected[cart_file] = json.load(expected_f)

        # Save BaseProductData with keys corresponding to the suffix of the 
        # filename, i.e, for base-prices-normal.json, the suffix is 'normal.json'
        for file in base_files:
            suffix = file.split("-")[-1]
            self.__base_prices[suffix] = BaseProductData(file)

    @classmethod
    def tearDownClass(self):
        '''
        Runs at the end of the TestCart call to perform clean-up duties. No
        real purpose at the moment as no side-effects take place but might need
        in the future.
        '''
        pass

    def test_totals(self):
        '''
        Tests for the total calculated values of Cart(s).
        For all loaded test cart files.

        Uses expected data files with suffix "-expected" in \fixtures 
        to determine correct values(s) from key 'count'. 

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.

        '''
        for cart_file in self.__carts:
            cart = self.__carts[cart_file]

            # Cart files and corresponding base-price files have the same suffix
            suffix = cart_file.split("-")[-1]
            base_prices = self.__base_prices[suffix]

            calculator = CLIPriceCalculator(cart, base_prices)

            real_total = calculator.cart_total
            expected_total = self.__expected[cart_file]["total_price"]

            self.assertEqual(real_total, expected_total)