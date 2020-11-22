
'''
__main__.py (entry-point)
CLI Redbubble Coding Test Price Calculator Program

Author: Redbubble Applicant
Email: me@example.com

README.md for more information.
'''
import json
import argparse
from cli_price_calculator_pkg.exceptions import CLIArgumentException

def extract_args():
    ''' 
    Returns the retrieved cart and base-prices JSON files from CLI.

    Args:
        None
    Returns:
        (tuple): Cart JSON file, base-prices JSON file 
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