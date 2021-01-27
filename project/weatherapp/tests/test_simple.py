# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import requests
# from sample.simple import add_one
import requests
import functools
class TestSimple(unittest.TestCase):

    def test_add_one(self):
        # self.assertEqual(add_one(5), 6)
        url = "http://127.0.0.1:8000/weather?serviceId=1"


        payload="{\n  \"lat\":33.3,\n  \"lon\":44.4,\n  \"unit\":\"C\"\n}"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.status_code)
        assert response.status_code == 200





if __name__ == '__main__':
    unittest.main()
