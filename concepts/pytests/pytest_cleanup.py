"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import pytest
from mongoengine import connect, disconnect


class Prod:

    def __init__(self, num):
        self.num = num

    def double_value(self):
        return self.num * 2


@classmethod
def setup_class(cls):
    connect('mongoenginetest', host='mongomock://localhost')

@classmethod
def teardown_class(cls):
    """set up Db
    """
    print("class tear down")
    disconnect()


@pytest.fixture
def num_fixture():
    p = Prod(10)
    print("setup up ", p.num)
    yield p
    p.num = 0
    print("clean up ", p.num)


def setup_method(self, method):
    """ setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class.
    """


def teardown_method(self, method):
    """ teardown any state that was previously setup with a setup_method
    call.
    """


def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    print("setup_function")


def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    print("teardown_function")


def test_doulble(num_fixture):
    assert 20 == num_fixture.double_value()


def test_doulble1(num_fixture):
    assert 20 == num_fixture.double_value()

