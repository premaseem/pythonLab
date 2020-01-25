__author__ = 'asee2278'

import requests

url = "http://127.0.0.1:5000/api/v1/address"
headers = {'content-type': 'application/json'}

payload_fail = open("payload_fail.json").read()
payload_pass = open("payload_pass.json").read()

# response = requests.request("POST", url, data=payload_fail, headers=headers)
# assert(response.status_code == 400)
#
response = requests.request("POST", url, data=payload_pass, headers=headers)
assert(response.status_code == 201)

# url = "http://127.0.0.1:5000/validator"
# payload_pass = open("mixed_payload_pass.json").read()
# response = requests.request("POST", url, data=payload_pass, headers=headers)
# assert(response.status_code == 400)

print("All tests passed")