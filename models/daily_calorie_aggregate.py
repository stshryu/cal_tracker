from models import calorie_intake
import success
from errors import errors

class DailyCalorieAggregate:
    def __init__(self):
        self.calorie_intakes = []
        self.total_calories = None

    def add_calorie_intake(self, cal_intake_obj):
        result = cal_intake_obj.validate()
        match result:
            case success.Success():
                self.calorie_intakes.append(cal_intake_obj)
            case errors.InputError():
                return result
            case _:
                return errors.UnexpectedError("Unexpected error adding calorie intake")

    def remove_calorie_intake(self, index_to_remove):
        size_of_list = len(self.calorie_intakes)
        if index_to_remove >= size_of_list:
            return errors.UnexpectedError("Index does not exist")
        else:
            self.calorie_intakes.pop(index_to_remove)

    def edit_calorie_intake(self, index_to_edit, updated_cal_obj):
        size_of_list = len(self.calorie_intakes)
        if index_to_edit >= size_of_list:
            return errors.UnexpectedError("Index does not exist")
        else:
            self.calorie_intakes[index_to_edit] = updated_cal_obj

    def calculate_calories(self):
        if len(self.calorie_intakes) == 0:
            self.total_calories = 0
        else:
            for intake in self.calorie_intakes:
                intake_total_cal = intake.calorie * intake.quantity
                self.total_calories += intake_total_cal

    def validate(self):
        if type(self.calorie_intakes) is not list:
            return False
        return True

    def map(self, schema):
        self.calculate_calories()
        try:
            mapped_object = schema(
                calorie_intakes=self.calorie_intakes,
                total_calories=self.total_calories
            )
            return success.Success(mapped_object)
        except Exception:
            return errors.UnexpectedError("Error mapping class to schema")

    def save(self, adapter, mapped_object):
        result = adapter.save(mapped_object)
        match result:
            case success.Success():
                return result
            case _:
                return result
