from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calinput', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form)
    else:
        return jsonify({"test": "hello_world"})
