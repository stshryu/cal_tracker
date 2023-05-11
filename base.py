from flask import Flask, request, jsonify
import pdb
from cal_calc import calculator

app = Flask(__name__)


@app.route('/calinput', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        response_dict = request.form.to_dict()
        food_name = response_dict['food_name']
        food_calories = calculator(food_name)
        return jsonify({"food_calories": food_calories})
    else:
        return jsonify({"test": "hello_world"})

