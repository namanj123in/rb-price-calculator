class PriceCalcException(Exception):
    
    def __init__(self, message = None):
        if message:
            self.__message = f"{self.__class__.__name__}: {message}"
        else:
            self.__message = f"{self.__class__.__name__} has been raised"

    def __str__(self):
        return self.__message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

class CLIArgumentException(PriceCalcException):
    def __init__(self, message = None):
        super().__init__(message = message)
class SchemaException(PriceCalcException):
    def __init__(self, message = None):
        super().__init__(message = message)

