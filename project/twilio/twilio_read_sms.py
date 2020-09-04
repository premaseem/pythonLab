from twilio.rest import Client
from datetime import datetime
import os

account_sid = os.environ["sid"]
auth_token = os.environ["token"]

twilio_from = os.environ["sender"]
twilio_to_1="+13257578316"
twilio_to_2="+18325583227"

# print(os.environ)
client = Client(account_sid, auth_token)
now = datetime.now()
print(now)

# Send SMS
message = client.messages.create(
    from_=twilio_from,
    body='Prem aseem test pin at {} : 1981 '.format(now),
    to=twilio_to_1
)

messages = client.messages.list(
    date_sent=now,
    from_= twilio_from,
    to=twilio_to_1,
    limit=1
)

for record in messages:
    print(record.body)

