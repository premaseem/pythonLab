"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""


# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com')

# print response
print(response)

# print elapsed time
print("Response time: ",round(response.elapsed.total_seconds(),2))
