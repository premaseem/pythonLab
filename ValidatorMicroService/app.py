__author__ = 'asee2278'

#!flask/bin/python
from flask import Flask, jsonify
from flask import make_response, request
from ValidatorMicroService.db.in_memory import address_list
from ValidatorMicroService.validator import SchemaValidator

app = Flask(__name__)

@app.route('/validator',methods=['POST'])
def validate_payload_against_schema():
    if not request.json:
        abort(400)
    validation_error = SchemaValidator.payload_validator(schema, request.json)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def payload_validation_failed(error):
    return make_response(jsonify({'error': 'Not found'}), 400)

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
    validation_error = SchemaValidator.payload_validator(schema, request.json)
    if len(validation_error) == 0:
        address_list.append(request.json)
        return jsonify({'address': request.json}), 201
    else:
        return jsonify({'payload_error': validation_error}), 400




if __name__ == '__main__':
    app.run(debug=True)


