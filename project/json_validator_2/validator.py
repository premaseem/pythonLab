"""
@author: Aseem Jain

@pip package
pip install jsonschema

Description:
Validate the json data against the schema for below validations:

# type of attribute - string / number

# Required property

# Optional property

# No additional property

# Validate array type
## homogenous array
## max items
## min items

# Nested objects with reusable schema
## required prop for nested objects

"""


import json
import jsonschema
from jsonschema import validate

# file path for json schema and data file
SCHEMA='data/schema1.json'
DATA="data/schema1-data.json"

def get_schema():
    """This function loads the given schema available"""
    with open(SCHEMA, 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


# Convert json to python object.
jsonData = json.loads('{"id" : 10,"name": "DonOfDen","contact_number":1234567890}')
with open(DATA) as json_file:
    jsonData = json.load(json_file)

# validate it
is_valid, msg = validate_json(jsonData)
print(msg)