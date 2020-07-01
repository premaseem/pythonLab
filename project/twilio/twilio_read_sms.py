from twilio.rest import Client
import os

account_sid = os.environ["sid"]
auth_token = os.environ["token"]
print(os.environ)
client = Client(account_sid, auth_token)

messages = client.messages.list(limit=20)

for record in messages:
    print(record.sid)
    print(record.body)

