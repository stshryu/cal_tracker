import json

class BaseError(Exception):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class UnexpectedError(BaseError):
    """
    Raised when an unexpected (uncaught) error is processed

    Attributes:
        message     -- message sent back with exception
    """

    def __init__(self, message="Unexpected error"):
        self.message = message

class InputError(BaseError):
    def __init__(self, inputs={}):
        self.inputs = inputs