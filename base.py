# Imports from libraries
from flask import Flask, request, jsonify
import success
from errors import errors

# Services and local imports
from cal_calc import calculator
from models import calorie_intake

# Initializing flask application
app = Flask(__name__)


@app.route('/get_calorie_count', methods=['POST'])
def get_calories():
    response_dict = request.form.to_dict()
    food_name = response_dict['food_name']

    result = calculator(food_name)
    match result:
        case success.Success():
            response = result.unpack()
            return jsonify(response)
        case errors.UnexpectedError():
            return jsonify(result.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Error"))


@app.route('/test', methods=['POST'])
def test():
    response_dict = request.form.to_dict()

    food_name = response_dict['food_name']
    food_calorie = response_dict['food_calorie']
    food_quantity = response_dict['food_quantity']

    cal_obj = calorie_intake.CalorieIntake(food_name, food_calorie, food_quantity)
    result = cal_obj.validate_and_save()
    breakpoint()
    match result:
        case success.Success():
            response = result.unpack()
            return jsonify(response)
        case errors.InputError():
            return jsonify(result.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Error"))
