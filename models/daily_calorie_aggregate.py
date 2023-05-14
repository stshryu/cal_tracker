import calorie_intake

class DailyCalorieAggregate:
    def __init__(self):
        self.calorie_intakes = []

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

