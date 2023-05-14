import success
from errors import errors

class CalorieIntake:
    def __init__(self, name, calorie, quantity):
        self.name = name
        self.calorie = calorie
        self.quantity = quantity

    def validate(self):
        validation_errors = {}
        if type(self.name) is not str:
            validation_errors['name'] = "Name must be a string"

        if not self.calorie.isdigit():
            validation_errors['calorie'] = "Calorie must be an int"
        else:
            self.calorie = int(self.calorie)

        if not self.quantity.isdigit():
            validation_errors['quantity'] = "Quantity must be an int"
        else:
            self.quantity = int(self.quantity)

        if len(validation_errors.keys()) == 0:
            return success.Success(True)

        else:
            return errors.InputError(validation_errors)

    def validate_and_save(self):
        result = self.validate()
        match result:
            case success.Success():
                return success.Success(self)
            case errors.InputError():
                return result
