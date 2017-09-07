__author__ = 'asee2278'

import json
import jsonschema

class SchemaValidator:

    def payload_validator(schema, data):
        try:
            v = jsonschema.Draft3Validator(json.loads(schema))
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