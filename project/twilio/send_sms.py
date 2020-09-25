from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0bb0b66d36f9716677d299f813507770'
auth_token = '<token>'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="Aseem testing number with Tim",
    from_='+15403601055',
    to='+19186952526'
)

print(message.sid)