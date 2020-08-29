import requests
from twilio.rest import Client

account = "xxx"
token = "xxx"

url1 = "https://prod-us.ci-twilio-proxy.com/"
url2 = "https://prod-uk.ci-twilio-proxy.com/"
url3 = "https://preprod.ci-twilio-proxy.com/"

client = Client(account, token)


def lambda_handler(event=None, context=None):
    try:
        r1 = requests.request("GET", url1)
        r2 = requests.request("GET", url2)
        r3 = requests.request("GET", url3)

        if r1.status_code != 400 or r2.status_code != 400 or r3.status_code != 400:
            client.messages.create(to="+12105109269", from_="+15128776881",
                                   body=" ALERT - AWS Twilo proxy down")
    except Exception as e:
        print(e)
        client.messages.create(to="+12105109269", from_="+15128776881",
                               body=" ALERT - AWS Twilo proxy down")

    print("""Health status is good :-) for AWS Twilio proxy 
    {}
    {}
    {}
    """.format(url1, url2, url3))


# lambda_handler()
