'''
test_cart.py
'''
import os
import json
import unittest
from os.path import join
from cli_price_calculator_pkg.cart import Cart

class TestCart(unittest.TestCase):
    '''
    Testing file for class Cart in main package cli_price_calculator_pkg.

    - Tests number of CartProduct(s) stored in Cart.
    - Tests content of CartProduct(s) using their str() representations.

    (The tests are conducted for sample test cart files stored in fixtures.)
    '''
    @classmethod
    def setUpClass(self):
        # Absolute path to \fixtures
        abs_path = join(os.getcwd(), "tests", "fixtures")

        # Read relevant test cart files from FILES.json in \fixtures
        with open(os.path.join(abs_path, "FILES.json"), "r") as f:
            loaded_json = json.load(f)
            cart_files = loaded_json["cart_files"]

        # For cart and expected test files, append path to ..\fixtures
        # to construct complete absolute paths to test files
        abs_cart_files = []
        expected_files = []
        for file in cart_files:
            abs_cart_path = join(abs_path, file)
            abs_cart_files.append(f"{abs_cart_path}.json")

            # For each cart file, the corresponding 'expected' data file is 
            # identified by the suffix '-expected' 
            expected_files.append(f"{abs_cart_path}-expected.json")

        self.__carts = {}
        self.__expected = dict(zip (abs_cart_files, expected_files))

        TestCart.load_test_files(abs_cart_files)
    
    @classmethod
    def load_test_files(self, cart_files):
        # Load cart files and the corresponding expected files
        for file in cart_files:
            self.__carts[file] = Cart(file)

        for cart_file, expected_file in self.__expected.items():
            with open(expected_file, "r") as expected_f:
                self.__expected[cart_file] = json.load(expected_f)

    @classmethod
    def tearDownClass(self):
        pass



    


