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
        Sets up the fixtures of test files and expected-result files to be 
        used for the following tests.

        Runs once when TestCart is called.

        Args:
            (self)
        Returns:
            None.
        '''
        # Absolute path to \fixtures
        self.abs_path = join(os.getcwd(), "tests", "fixtures")

        # Read relevant test cart files from FILES.json in \fixtures
        with open(os.path.join(self.abs_path, "NORMAL_FILES.json"), "r") as f:
            loaded_json = json.load(f)
            cart_files = loaded_json["cart_files"]

        # For cart and expected test files, append path to ..\fixtures
        # to construct complete absolute paths to test files
        abs_cart_files = []
        expected_files = []
        for file in cart_files:
            abs_cart_path = join(self.abs_path, file)
            abs_cart_files.append(f"{abs_cart_path}.json")

            # For each cart file, the corresponding 'expected' data file is 
            # identified by the suffix '-expected' 
            expected_files.append(f"{abs_cart_path}-expected.json")

        self.__carts = {}
        # Associate each file with corresponding expected-result file
        self.__expected = dict(zip (abs_cart_files, expected_files))

        TestCart.load_test_files(abs_cart_files)
    
    @classmethod
    def load_test_files(self, cart_files):
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

    @classmethod
    def tearDownClass(self):
        '''
        Runs at the end of the TestCart call to perform clean-up duties. No
        real purpose at the moment as no side-effects take place but might need
        in the future.
        '''
        pass

    ################################  TESTS  ##################################

    def test_cart_counts(self):
        '''
        Tests for the quantity of items stored in 'normal' Cart(s) - originally
        supplied.

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
            real_count = self.__carts[cart_file].get_count()
            expected_file = self.__expected[cart_file]
            expected_count = expected_file["count"]
            self.assertEqual(real_count, expected_count)

    def test_cart_contents(self):
        '''
        Tests for the contents of items stored in normal Cart(s).
        For all loaded test cart files.

        Uses expected data files with suffix "-expected" in \fixtures 
        to determine correct values(s) from key 'cart_str'. 

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        for cart_file in self.__carts:
            real_content_str = str(self.__carts[cart_file]).strip()
            expected_str = self.__expected[cart_file]["cart_str"]
            self.assertEqual(real_content_str, expected_str)

    def test_empty_cart(self):
        '''
        Tests for cart count and contents of an empty cart.

        Args:
            (self)
        Returns:
            None.
        Raises:
            AssertionError: if test fails.
        '''
        self.general_test_runner("cart-0-empty.json")
                                 "cart-0-empty-expected.json"
                                 )

    def general_test_runner(self, cart, expected):
        '''
        A general test runner for cart count and content tests. 
        Checks if the cart content and quantity is correct.

        Args:
            cart (str): JSON file of test cart.
            expected (str): JSON file of expected test cart file.
        Returns:
            None.
        '''
        test_cart = join(self.abs_path, cart)
        expected = join(self.abs_path, expected)

        with open(expected, "r") as f:
            expected_json = json.load(f)

        cart = Cart(test_cart)
        self.assertEqual(cart.get_count(), expected_json["count"])
        self.assertEqual(str(cart).strip(), expected_json["cart_str"])

    



    


