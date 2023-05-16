from models import calorie_intake
import success
from errors import errors

class DailyCalorieAggregate:
    def __init__(self):
        self.calorie_intakes = []

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

    def validate(self):
        if type(self.calorie_intakes) is not list:
            return False
        return True

    def validate_calorie_list(self):
        """
        Expensive operation to validate every calorie intake in the aggregate
        :return:
        Boolean
        """
        for item in self.calorie_intakes:
            if type(item) is not calorie_intake.CalorieIntake:
                return False
        return True

    def save(self, adapter):
        result = adapter.save(self)
        match result:
            case success.Success():
                return result
            case _:
                return result


