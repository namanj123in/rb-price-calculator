'''
product_data.py
'''
import json
import sys

class BaseProductData:
    '''
    Implementation of BaseProductData as a representation of a Redbubble 
    base-prices database.
    - Loads data from provided base-prices JSON.
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
        first_option_type = options_tuples[0]
        # List of option values ex. 'small', 'xl', corresponding to the first
        # option type of options_tuples
        options = first_option_type[1]

        for option in options:
            # Base case: last option type
            if len(options_tuples) == 1:
                # For the last option, the values are base-prices i.e, 'leafs'
                # of the tree
                level[option] = base_price
            else:
                if option not in level:
                    level[option] = {}

                self.generate_tree_helper(level[option], options_tuples[1:], \
                                            base_price)

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

