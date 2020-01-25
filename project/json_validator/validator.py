__author__ = 'asee2278'

import json
import jsonschema

schema = open("schema.json").read()
# print (schema)

# data = open("data.json").read()
data = open("data-error.json").read()
# print (data)

# try:
#     jsonschema.validate(json.loads(data), json.loads(schema))
# except jsonschema.ValidationError as e:
#     print (e.message)
# except jsonschema.SchemaError as e:
#     print (e)


# report all errors in the instance
try:
    v = jsonschema.Draft3Validator(json.loads(schema))
    validation_error = []
    for error in sorted(v.iter_errors(json.loads(data)), key=str):
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
