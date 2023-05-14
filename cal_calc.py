import success
from errors import errors

database = {
    "apple": "100",
    "orange": "200",
    "sliced_bread": "300"
}


def calculator(food):
    if food in database:
        return success.Success({"food_calories": database[food]})
    else:
        return errors.UnexpectedError("No food found in database")