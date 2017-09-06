__author__ = 'asee2278'

#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response, request
import json
import jsonschema

app = Flask(__name__)

address_list = [
    {
        "address":{
            "streetAddress": "4114 Medical Drive",
            "city":"San Antonio",
            "houseNumber":12
        },
        "phoneNumber":
            [
                {
                    "type":"home",
                    "number":"212 555-1234"
                }
            ]
    },
    {
        "address":{
            "streetAddress": "21 2nd Street",
            "city":"New York",
            "houseNumber":12
        },
        "phoneNumber":
            [
                {
                    "type":"home",
                    "number":"212 555-1234"
                }
            ]
    }
]


def payload_validator(schema, data):
    try:
        v = jsonschema.Draft3Validator(json.loads(schema))
        validation_error = []
        for error in sorted(v.iter_errors(data), key=str):
            property = str(error.path).replace("deque","",1)
            if "required" not in error.message:
                message = str("value {} for property {}".format(error.message, property))
                print(message)
                validation_error.append(message)
            else :
                print(error.message)
                validation_error.append(error.message)
                # print(validation_error)

    except jsonschema.ValidationError as e:
        print (e.message)
    return validation_error


@app.route('/')
def index():
    return "Welcome to Validator micro service"

@app.route('/api/v1/address', methods=['GET'])
def get_tasks():
    return jsonify({'address': address_list})

@app.route('/api/v1/address', methods=['POST'])
def create_task():

    if not request.json:
        abort(400)
    schema = open("schema.json").read()
    validation_error = payload_validator(schema, request.json)
    if len(validation_error) == 0:
        address_list.append(request.json)
        return jsonify({'address': request.json}), 201
    else:
        return jsonify({'payload_error': validation_error}), 400


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def payload_validation_failed(error):
    return make_response(jsonify({'error': 'Not found'}), 400)

if __name__ == '__main__':
    app.run(debug=True)


