#
# $ python verify_twilio_phone_numbers.py -f

# Script accepts a json file as input argument to script.
# run twilo validation on data
# generates a final report
# Final Report to find non serviceable Twilio mobile number
# ======================
# Total Users with MFA as SMS 12
# Twilio Supported MFA users 10
# Twilio Supported MFA users  2



import requests
import json
import argparse
import sys

headers = {
    'Authorization': 'Basic xxx=='
}

class VerifyTwilioNumbers():

    def __init__(self, users_list):
        self.num_list = users_list
        self.invalid_users_list = []
        self.total_records = len(self.num_list)
        self.valid_records = 0

        print(self.total_records, " are total number of records ")

    def process_verification(self):
        for data in self.num_list:
            self.verify_number(data)

    def verify_number(self, user_info):
        phone_num = user_info.get("phone_number")
        url = "https://lookups.twilio.com/v1/PhoneNumbers/{}".format(phone_num)

        try:
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                self.valid_records += 1
            else:
                print("INVALID mobile_number: {} user_id: {} in domain {}".format(phone_num, user_info.get("user_id"),
                                                                                  user_info.get("user_domain_id")))
                self.invalid_users_list.append(user_info)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # file_path = "/Users/asee2278/git/twilio-relatred /twilio-data-stage/test_data.json"
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_path")
    args = parser.parse_args()

    if not args.file_path:
        sys.exit()

    with open(args.file_path) as f:
        user_data = json.load(f)

    obj = VerifyTwilioNumbers(user_data)
    obj.process_verification()
    report = ""
    report += "\nFinal Report to find non serviceable Twilio mobile number"
    report += "\n======================"
    report += "\nTotal Users with MFA as SMS {}".format(str(obj.total_records))
    report += "\nTwilio Supported MFA users {}".format(str(obj.valid_records))
    report += "\nTwilio Supported MFA users  {}".format(str(len(obj.invalid_users_list)))

    print(report)
    with open("report.txt", "w") as f:
        f.write(report)
        f.write("\n======================")
        f.write("Invalid Users details are: \n")
        json.dump(obj.invalid_users_list, f)
