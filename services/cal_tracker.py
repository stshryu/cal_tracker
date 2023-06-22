import models.calorie_intake as calorie_intake
import success
from errors import errors


def create_calorie_intake(name, calorie, quantity):
    temp_calorie_intake = calorie_intake.CalorieIntake(name, calorie, quantity)

    result = temp_calorie_intake.validate_and_save()
    match result:
        case success.Success():
            return result
        case errors.InputError():
            return result

# def add_to_aggregate(aggregate, calorie_intake):
#     result = aggregate.
