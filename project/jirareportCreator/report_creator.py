__author__ = 'aseem Jain'

# script fetch all issues in Jira board and calculate


# Outputs in below format
# /Users/asee2278/virtualEnv/nisEnv/bin/python /Users/asee2278/gitRepo/masterFork/nis/nis_api/lib/v2/salesforce.py
# Number of Issues in New/In Analysis are 147
# Number of Issues in RF Dev are 6
# Number of Issues in In Progress are 26
# Number of Issues in RF PR are 2
# Number of Issues in In Review are 7
# Number of Issues in RF Test/UAT are 0
# Number of Issues in In Test / UAT are 4
# Number of Issues in RF Deploy are 0
# Number of Issues in Closed are 60
#
# Process finished with exit code 0

import requests
import json
import urllib3

urllib3.disable_warnings()

base_url = "https://jira.com"
user = 'asee2278'
password = 'XXX'
jql = 'rest/greenhopper/1.0/xboard/work/allData.json?rapidViewId=2630&selectedProjectKey=BAREMETAL&_=1513179039405'
new_url = base_url + jql


def get_all_urls():

    json_response = fetchUrl(new_url)

    cloumns = json_response['columnsData']['columns']

    # add additional attribute of count
    for cloumn in cloumns:
        cloumn['count'] = 0

    issues = json_response['issuesData']['issues']

    for issue in issues:
        calculate_issue_count(cloumns, issue)

    print_result(cloumns)


def print_result(cloumns):
    for cloumn in cloumns:
        print("Number of Issues in {} are {}".format(cloumn['name'], cloumn['count']))


def calculate_issue_count(cloumns, issue):
    for cloumn in cloumns:
        if issue['statusId'] in cloumn['statusIds']:
            cloumn['count'] += 1


def fetchUrl(url):

    response = requests.get(url, verify=False, auth=(user, password))
    json_response = json.loads(response.text)

    return json_response


get_all_urls()