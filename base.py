# Imports from libraries
from flask import Flask, request, jsonify
import success
from errors import errors

# Services and local imports
from models import daily_calorie_aggregate
from models import calorie_intake

# Initializing flask application
app = Flask(__name__)


@app.route('/add_food', methods=['POST'])
def add_to_daily_calorie_aggregate():
    response_dict = request.form.to_dict()
    food_name = response_dict['food_name']

    # Create calorie intake object
    cal_intake_object = calorie_intake.CalorieIntake()
    #result =

    # Create a daily calorie aggregate
    daily_calorie_object = daily_calorie_aggregate.DailyCalorieAggregate()
    result = daily_calorie_object.add_calorie_intake()
    match result:
        case success.Success():
            response = result.unpack()
            return jsonify(response)
        case errors.UnexpectedError():
            return jsonify(result.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Error"))
