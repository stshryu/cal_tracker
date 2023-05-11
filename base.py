from flask import Flask, request, jsonify
import success
from errors import errors

from cal_calc import calculator

app = Flask(__name__)


@app.route('/calinput', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
                return jsonify({"test": "test"})
    else:
        return jsonify({"test": "hello_world"})

