'''
exceptions.py
'''
class PriceCalcException(Exception):
    '''
    Generic Exception class for PriceCalculator.
    '''
    def __init__(self, message = None):
        '''
        Constructor for Cart - intialise message string.

        Args:
            (str): Return message for the exception when raised.
        Returns:
            None.
        '''
        if message:
            self.__message = f"{self.__class__.__name__}: {message}"
        else:
            # Default message
            self.__message = f"{self.__class__.__name__} has been raised"

    def __str__(self):
        '''
        String representation of Exception -> the message value.

        Args:
            (self)
        Returns
            (str): Exception message
        '''
        return self.__message

    @property
    def message(self):
        '''
        Property-based Getter for message.

        Args:
            (self)
        Returns
            (str): Exception message.
        '''
        return self.__message

    @message.setter
    def message(self, value):
        '''
        Property-based Setter for message.

        Args:
            value (str): New message
        Returns
            None.
        '''
        self.__message = value

class CLIArgumentException(PriceCalcException):
    '''
    Used to represent command-line-based exceptions.
    '''
    def __init__(self, message = None):
        super().__init__(message = message)
        
class SchemaException(PriceCalcException):
    '''
    Used to represent exceptions related to incompatible schemas for the input
    JSON files. 
    
    Like, duplicate products in base-prices with different prices.
    '''
    def __init__(self, message = None):
        super().__init__(message = message)

