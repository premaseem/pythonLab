import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox73ee7356c3494cb48935554b7a7b4ada.mailgun.org/messages",
        auth=("api", "xxx"),
        data={"from": "aseem.jain@rackspace.com",
              "to": ["aseem.jain@rackspace.com", "aseem.jain@rackspace.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

res = send_simple_message()
print(res)