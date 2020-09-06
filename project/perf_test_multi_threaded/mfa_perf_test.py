import requests
import json
import datetime
from twilio.rest import Client
from datetime import datetime
import os
import time
import _thread

# Test users
# twilio_to_1="+13257578316"
# twilio_to_2="+18325583227"
MAX_REQ=1000
cnt = 0

class MFA:
    url = "<end point>"
    account_sid = os.environ["sid"]
    auth_token = os.environ["token"]
    twilio_from = os.environ["sender"]

    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.session_id = None
        self.pin = None
        self.attempt = 0

    def auth_step_1(self):
        payload = {
            "auth": {
                "passwordCredentials": {
                    "username": self.username,
                    "password": self.password
                }
            }
        }
        response = requests.request("POST", MFA.url, headers={
            'Content-Type': 'application/json'
        }, data=json.dumps(payload))
        if response.status_code != 401:
            return False
        self.session_id = response.headers['WWW-Authenticate'][17:-20]
        return True


    def read_sms_pin(self, dt):
        self.attempt += 1
        time.sleep(1)
        client = Client(MFA.account_sid, MFA.auth_token)
        messages = client.messages.list(
            date_sent=dt,
            from_=MFA.twilio_from,
            to=self.phone_number,
            limit=1
        )
        # if message is not there wait for 5 more sec
        return messages



    def auth_mfa_setup2(self):

        headers_step_2 = {
        'Content-Type': 'application/json',
        'X-SessionId': self.session_id
        }

        payload_step_2 = {
            "auth": {
                "RAX-AUTH:passcodeCredentials": {
                    "passcode": self.pin
                }
            }
        }

        response = requests.request("POST", self.url, headers=headers_step_2, data = json.dumps(payload_step_2))
        if response.status_code == 200:
            return True
        return False

    # user1 id: f96b788a6fb74f309348acf18dcf02d1

    def run(self):
        now = datetime.now()
        if self.auth_step_1():
            msgs = self.read_sms_pin(now)

            while len(msgs) != 1:
                msgs = self.read_sms_pin(now)
                if self.attempt > 10:
                    return False
            self.pin = msgs[0].body.strip()[-7:]
            # self.attempt = 0

            if self.auth_mfa_setup2():
                return True
        return False

    def __str__(s):
        global cnt
        cnt += 1
        result = " {}  - Request number {} took {} attempts to read sms for Number {} with session id {}".format(datetime.now(), cnt, s.attempt,s.phone_number, s.session_id)
        return result


f = open("result.txt","a+")

def execute(tname,un):
    for i in range(MAX_REQ//2):
        test_obj = MFA(un, "<password>", "+1"+un)
        if test_obj.run():
            result = "Passed: " + str(test_obj) + " in " + tname
        else:
            result = "Failed: " + str(test_obj) + " in " + tname
        print(result)
        f.write(result + "\n")



# Create two threads
try:
    _thread.start_new_thread( execute, ("Thread-1 ", "3257578316" ) )
    _thread.start_new_thread( execute, ("Thread-2 ", "8325583227" ) )
except:
    print ("Error: unable to start thread")


while 1:
    pass