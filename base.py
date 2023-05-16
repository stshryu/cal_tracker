# Imports from libraries
from flask import Flask, request, jsonify
import success
from errors import errors

# Services and local imports
from cal_calc import calculator

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
