from twilio.rest import Client
import os

account_sid = os.environ["sid"]
auth_token = os.environ["token"]
print(os.environ)
client = Client(account_sid, auth_token)

phone_number = client.lookups.phone_numbers('2105109269').fetch(country_code='US')

print(phone_number.phone_number)