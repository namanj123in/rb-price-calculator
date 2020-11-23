'''
__main__.py (entry-point)
CLI Redbubble Coding Test Price Calculator Program

Author: Redbubble Applicant
Email: me@example.com

README.md for more information.
'''
import sys
import json
import argparse
from cli_price_calculator_pkg.cart import Cart
from cli_price_calculator_pkg.exceptions import CLIArgumentException
from cli_price_calculator_pkg.product_data import BaseProductData
from cli_price_calculator_pkg.cli_price_calculator import CLIPriceCalculator

def extract_args():
    ''' 
    Returns the retrieved cart and base-prices JSON files from CLI.

    Args:
        None
    Returns:
        (tuple): cart JSON file, base-prices JSON file 
    Raises:
        CLIArgumentException - for missing JSON file paths.
    '''
    parser = argparse.ArgumentParser(description="RedBubble CLI price \
                calculator program. Calculates total price for a 'cart' given \
                base-prices. Need cart and base-prices JSON files.")

    parser.add_argument("cart", nargs="?", help="Cart JSON file")
    parser.add_argument("base_prices", nargs="?", help="Base Prices JSON file")

    args = parser.parse_args()

    if not args.cart:
        raise CLIArgumentException(message = "Missing cart JSON file.")
    if not args.base_prices:
        raise CLIArgumentException(message = "Missing base-prices JSON file.")

    return args.cart, args.base_prices

def main():
    '''
    Driver program to calculate the total cart price.

    Args:
        None
    Returns:
        (int): The total price amount of cart in cents
    Raises:

    '''
    try:
        cart_json, prices_json = extract_args()
    except CLIArgumentException as error:
        sys.exit(error.message)

# ################ CART ####################
    cart = Cart(cart_json)
    print(cart)

# ########## BASE-PRICES DATA ##############
    prices = BaseProductData(prices_json)

    print(json.dumps(str(prices), indent=8))

# ############ PRICE CALCULATOR ############
    calculator = CLIPriceCalculator(cart, prices)

    print(f"{calculator.cart_total}\n")


################################### MAIN #######################################
main()