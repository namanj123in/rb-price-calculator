'''
product_data.py
'''
import json
import sys
from cli_price_calculator_pkg.exceptions import SchemaException

class BaseProductData:
    '''
    Implementation of BaseProductData as a representation of a Redbubble 
    base-prices database.
    - Loads data from provided base-prices JSON.
    - Generates a nested-dict tree-like structure to retrieve base-price(s) of
      requested CartProducts independent of the quantity of base-prices. 
    - Retrieves base-price of a requested CartProduct

      More information in generate_price_tree().
    '''

    def __init__(self, json_prices):
        self.__json_prices = json_prices
        self.__loaded_prices = self.load_prices()
        self.__count = 0

        self.__price_tree, self.__relevant_options = self.generate_price_tree()

    def load_prices(self):
        '''
        Loads base-prices JSON returned to and stored by self.__loaded_prices.

        -> Can cause early exit, if unable to load JSON file.

        Args:
            (self)
        Returns:
            (dict): JSON data from base-prices JSON.
        '''
        try:
            with open(self.__json_prices, "r") as prices_f:
                prices_data = json.load(prices_f)
        except:
            sys.exit(f"Something went wrong! Could not load {self.__json_prices}")
        return prices_data

    def generate_price_tree(self):
        '''
        Generates a nested-dict structure with product_types as keys at 
        top-level and base-price values at the bottom-levels ('leaf' values).
        Each subsequent nested-dict contains keys of a specific option-type.

        Each base value is reachable via a combination of product-type and 
        option-values, causing the process of retrieving a base-price
        for a requested CartProduct to be dependent on the number of option
        types for the CartProduct and not dependent on the number of 
        base-prices.

        Calls recursive function generate_price_helper().

        For a more visual explanation, check "Key Algorithms" in README.

        Args:
            (self)
        Returns:
            price_tree (nested-dict), 
            relevant_options (dict) (from product-type to list of option-types) 
        '''
        price_tree = {}
        relevant_options = {}
        for price_product in self.__loaded_prices:
            self.__count += 1
            product_type = price_product["product-type"]
            product_options = price_product["options"]
            product_price = price_product["base-price"]

            # First occurence of product_type -> initialise value in 
            # price_tree and relevant_options
            if product_type not in price_tree:
                price_tree[product_type] = {}
                relevant_options[product_type] = []

            options_tuples = []
            for option_type, options in product_options.items():
                # Record relevant option types for current product_type
                if option_type not in relevant_options[product_type]:
                    relevant_options[product_type].append(option_type)

                options_tuples.append((option_type, options))

            if options_tuples:
                options_tuples = sorted(options_tuples)
                self.generate_tree_helper(price_tree[product_type], \
                                          options_tuples, product_price)
            else:
                # If no options, the top-level is the last, ie. contains
                # base-prices.
                price_tree[product_type] = product_price

        return price_tree, relevant_options
            
    def generate_tree_helper(self, level, options_tuples, base_price):
        '''
        Algorithm to recursively build the levels of the price_tree by calling
        itself for each option-value (like, "small" for option-type "size") 
        with the next level and remaining option-types as arguments.

        Stops when all option-types for the current product are exhausted, and
        then uses the base-prices as values (at the last level).

        Args:
            level (dict): the current dict in price_tree
            options_tuples ([tuple]): list of tuples with first value being
                                      option-type (ex. "size") and second value
                                      being a list of corresponding options
                                      (like ["small", "big"]), corresponding to
                                      a product-object in base-prices
            base_price (int): base-price of the product

        Returns:
            None: (creates the price_tree by reference from argument, level)

        Raises:
            SchemaException: if the exact same product-type, options
                             combination is encountered but with a different 
                             base-price.
        '''
        first_option_type = options_tuples[0]
        # List of option values ex. 'small', 'xl', corresponding to the first
        # option type of options_tuples
        options = first_option_type[1]

        for option in options:

            # Base case: last option type
            if len(options_tuples) == 1:

                # For the last option, the values are base-prices i.e, 'leafs'
                # of the tree
                if option in level and level[option] != base_price:
                    raise SchemaException("Same base-product has different base values.")
                else:
                    level[option] = base_price
            else:

                if option not in level:
                    level[option] = {}

                # Call helper on the remaining option_tuples and the next 
                # 'level' in the nested-dict structure
                self.generate_tree_helper(level[option], options_tuples[1:], \
                                            base_price)

    def cart_product_base_price(self, cart_product):
        '''
        Return the base-price of cart_product by tracing the route from
        its product-type and option-values to the base-price at the final
        level in the price_tree.

        Args:
            (CartProduct): Product to get the base-price of
        Returns:
            (int): Base-price for the product
        Raises:
            SchemaException: If a valid route to a base-price cannot be found
        '''
        product_type = cart_product.product_type
        option_tuples = cart_product.options_tuples()

        # Filter out any option types not found in self.__price_tree
        option_tuples = filter(lambda x: self.is_relevant(x, product_type), \
                                option_tuples)

        # Retain the same key order as self.__price_tree of CartProduct's 
        # options
        option_tuples = sorted(option_tuples)

        # Follow path from 'root' to 'leaf' via option values of cart product 
        tree_level = self.__price_tree[product_type]
        try:
            for option_tuple in option_tuples[:-1]: 
                option_val = option_tuple[1]
                tree_level = tree_level[option_val]

            # The 'leaf' values are the base- -prices, by definition
            last_option_val = option_tuples[-1][1]
            base_price = tree_level[last_option_val]
        except (KeyError, IndexError):
            raise SchemaException(f"Incorrect option values for - {cart_product}")

        return base_price

    def is_relevant(self, option_tuple, product_type):
        '''
        Used in filter lambda function in cart_product_base_price() above.
        
        Args:
            option_tuple (tuple): tuple of option_type, corresponding values
            product_type (str): type of the product
        Returns:
            (Bool): Whether the option type is relevant to the product-type
                    in respect to the price_tree.
        '''
        option_type = option_tuple[0]
        return option_type in self.__relevant_options[product_type]

    ##############################  Properties  ################################

    @property
    def price_tree(self):
        '''
        Property-based Getter for price_tree. Returns the dictionary structure,
        as explained above.

        Args:
            (self)
        Returns
            (dict->dict->..): Nested-Dicts -> price_tree.
        '''
        return self.__price_tree

    @property
    def count(self):
        '''
        Property-based Getter for quantity of base-prices.

        Args:
            (self)
        Returns
            (int): Number of base-prices.
        '''
        return self.__count

    @property
    def relevant_options(self):
        '''
        Property-based Getter for relevant_options. Returns a dictionary with 
        product-types as keys and list of distinguishing option types as values.

        To be able to recognise, for a CartProduct, whether a certain option
        is relevant or not in retrieving its base-price.

        Args:
            (self)
        Returns
            (dict): str:[str], From product-types to option types, 
                             like {"hoodie": ["size", "colour"]}
        '''
        return self.__relevant_options

    def __str__(self):
        '''
        String representation (str()) of product_data. Since, price_tree is a 
        nested-dict structure, its default __str__ representation can be
        returned and will be used to represent product_data.

        Args:
            (self)
        Returns
            (str): String representation of price_tree.
        '''
        return str(self.__price_tree)

