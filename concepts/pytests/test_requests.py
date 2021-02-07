"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import pytest
import requests
import requests_mock

## Production code ##
__BASE_URL = "http://test.com"


def get_employee(id):
    resp = requests.get(f'{__BASE_URL}/employee/{id}')
    if resp.status_code == 404:
        return None

    return resp.json()


## Production code ##


@pytest.fixture
def resp_1():
    return {"id": "test", "name": "test name"}


def test_get_employee(requests_mock, resp_1):
    test_id = "12345"
    resp_json = resp_1
    requests_mock.get(f'{__BASE_URL}/employee/{test_id}', json=resp_json)
    resp = get_employee(test_id)
    print(resp, "aseem")


def test_get_employee1(requests_mock):
    test_id = "98765"
    requests_mock.get(f'{__BASE_URL}/employee/{test_id}', status_code=404)
    resp = get_employee(test_id)
    print(resp, "aseem")
