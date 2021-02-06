"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import pytest

# Setup and Tear down fixtures
@pytest.fixture()
def data_service():
    print("setup objexts")
    yield [1,2,3,4]
    print("clean up date")

def test_sum(data_service):
    assert 10 == sum(data_service)

