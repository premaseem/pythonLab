__author__ = 'asee2278'

import json
import jsonschema

class SchemaValidator:

    def payload_validator(self,schema, data):
        try:
            if type(data) is not dict:
                data = json.loads(data)
            if type(schema) is not dict:
                schema = json.loads(schema)

            v = jsonschema.Draft3Validator(schema)
            validation_error = []

            for error in sorted(v.iter_errors(data), key=str):
                property = str(error.path).replace("deque", "", 1)
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

    def validator(self,schema, data):
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