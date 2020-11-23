# Redbubble Coding Test - CLI Price Calculator

CLI Price Calculator is a Python command-line program for calculating the total price of items in a cart given the `cart` and `base-prices` information JSON files. The expected formats can be found under the `schema` directory. 

The program is implemented in response to the **Redbubble Software Engineer** coding test and, accordingly, all elements of the program specification, including the provided sample files, are under the ownership of **Redbubble**.

http://take-home-test.herokuapp.com/new-product-engineer

## Directory Structure
```bash
├── Schema                   
├──  cli_price_calculator_pkg   
    ├── __init__.py
    ├── __main__.py
    ├── cart_product.py
    ├── cart.py
    ├── cli_price_calculator.py
    ├── exceptions.py
    └── product_data.py
├── tests                
    ├── fixtures
        └── [sample tests and expected *.json files]
    ├── test_case.py
    ├── test_calculator.py
    └── test_product_data.py
├── .gitignore           
├── README.md           
└── setup.py
```

## Requirement
Python version >= 3.2.5, setup.py for more information.

*Developed with Python 3.8.5*.

#### Libraries:
- unittest (built-in)
- json (built-in)
- os & os.path (built-in) - for testing
- argparse (built-in for Python >= 2.7)

## Installation | Usage

To run the module, run from the top-level directory (i.e., folder containing README.md), depending on your Python env and/or config settings:

```bash
python3 -m cli_price_calculator_pkg <path_to_cart_json> <path_to_base_prices_json>
```
or (if Python >= 3.2.5 is default or aliased):

```bash
python -m cli_price_calculator_pkg <path_to_cart_json> <path_to_base_prices_json>
```
**The order of the arguments is important.**

Run ```python -m cli_price_calculator_pkg -h``` for a more verbose description.

For all commands mentioned, keyword `python` will serve as a placeholder for `python` or `python3`. Use the Python command that you used to run the module.

*For the purposes of building the package and generating distribution archives (for Package Index), a setup.py file is also included. However, it is not necessary for running the module or the tests.*  

## Testing

Automated testing is implemented via. Python's `unittest` framework. All testing files are located under directory `tests`. Test classes are split across the `Cart (cart.py)`, `BaseProductData (product_data.py)`, and `CLIPriceCalculator (cli_price_calculator.py)` classes inside `cli_price_calculator_pkg` package directory.

Sample testing files and corresponding expected data are stored under `.\tests\fixtures` as JSON files.

To run the entire test-suite (again from the top-level folder):
```bash
python -m unittest discover tests -v
```

To run a single test file:
```bash
python -m unittest tests.<test_file_name> -v
```
Example:
```bash
python -m unittest tests.test_cart -v
```

## Key Algorithms
