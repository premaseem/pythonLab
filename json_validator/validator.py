__author__ = 'asee2278'

import json
import jsonschema

schema = open("schema.json").read()
# print (schema)

data = open("data.json").read()
# data = open("data-error.json").read()
# print (data)

try:
    jsonschema.validate(json.loads(data), json.loads(schema))
except jsonschema.ValidationError as e:
    print (e.message)
except jsonschema.SchemaError as e:
    print (e)

# # Use a Draft3Validator
# try:
#     jsonschema.Draft3Validator(json.loads(schema)).validate(json.loads(data))
# except jsonschema.ValidationError as e:
#     print (e.message)
#
#
# # Lazily report all errors in the instance
# try:
#     v = jsonschema.Draft3Validator(json.loads(schema))
#     for error in sorted(v.iter_errors(json.loads(data)), key=str):
#         print(error.message)
# except jsonschema.ValidationError as e:
#     print (e.message)
