import json
import os
import success

CONST_FILEPATH = "../json_file_output.json"

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, CONST_FILEPATH)

def save(save_object):
    base_array = []
    for obj in save_object.calorie_intakes:
        base_array.append(obj.__dict__)
    result = json.dumps(base_array)
    write_to_file(result, file_path)
    return success.Success(True)


def write_to_file(json_object, path):
    with open(path, 'w') as file:
        file.write(json_object)