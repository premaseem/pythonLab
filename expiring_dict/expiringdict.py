__author__ = 'asee2278'

# ~*~ coding: utf-8 ~*~
"""
This module is responsible to fetch token from mongodb which can be used by application for sales force and other calls.
TODO: This module will self generate tokens based on service account credentials and cache them at application level.
Returns None when value expires.
"""

__author__ = 'asee2278'


from expiringdict import ExpiringDict

import time

class TokenGenerator(object):

    def __init__(self):
        self.cache = ExpiringDict(max_len=200, max_age_seconds=1)
        # self.cache['auth_token'] = "1234"

    def get_token(self):
        auth_token = self.cache.get('auth_token')
        return auth_token


    def generate_token(self):
        self.cache['auth_token'] = "1234"
        return "1234"



token = TokenGenerator()
token.generate_token()
t= token.get_token()

print(t)
time.sleep(3)

t= token.get_token()
print(t)

token.generate_token()
t= token.get_token()
print(t)