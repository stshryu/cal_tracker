# Imports from libraries
from flask import Flask, request, jsonify
import success
from errors import errors
from sqlalchemy import create_engine

# Services and local imports
from models import daily_calorie_aggregate
from models import calorie_intake
from schemas.schemas import Base
from schemas.schemas import DailyCalorieAggregates, CalorieIntakes
from models.adapters import postgres_adapter as adapter

# Initializing flask application
app = Flask(__name__)

# Initializing the database connection
#conn_url = 'postgresql+psycopg2://test_user:Testing123!@db:5432/test_db'
#engine = create_engine(conn_url)
#Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)

@app.route('/create_aggregate', methods=['POST'])
def create_daily_calorie_aggregate():
    # Create a daily calorie aggregate
    daily_calorie_object = daily_calorie_aggregate.DailyCalorieAggregate()

    # Map the daily calorie aggregate to a schema
    mapped_result = daily_calorie_object.map(DailyCalorieAggregates)
    match mapped_result:
        case success.Success():
            mapped_object = mapped_result.unpack()
        case errors.UnexpectedError():
            return jsonify(mapped_result.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Errorl"))

    # Save the mapped object to DB
    saved_object = daily_calorie_object.save(adapter, mapped_object)

    # Return the ID of the created calorie aggregate 
    match saved_object:
        case success.Success():
            response = saved_object.unpack()
            return jsonify({ 'id': response })
        case errors.UnexpectedError():
            return jsonify(result.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Error"))


@app.route('/add_food', methods=['POST'])
def add_to_daily_calorie_aggregate():
    response_dict = request.form.to_dict()
    food_name = response_dict['food_name']
    food_calories = response_dict['food_calories']
    food_quantity = response_dict['food_quantity']

    # Create calorie intake object
    cal_intake_object = calorie_intake.CalorieIntake(food_name, food_calories, food_quantity)
    validated_intake = cal_intake_object.validate_and_save()

    match validated_intake:
        case success.Success():
            cal_intake = validated_intake.unpack()
        case errors.UnexpectedError():
            return jsonify(validated_intake.toJson())
        case errors.InputError():
            return jsonify(validated_intake.toJson())
        case _:
            return jsonify(errors.UnexpectedError("Unexpected Error"))
