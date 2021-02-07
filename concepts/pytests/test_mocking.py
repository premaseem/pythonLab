"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

from time import sleep

# class Applicaton:
def is_windows():
        # This sleep could be some complex operation instead
        sleep(1)
        return True

def get_operating_system():
    if is_windows():
        return 'Windows'
    else :
        return "linux"


# 'mocker' fixture provided by pytest-mock
def test_get_operating_system(mocker):
    mocker.patch('test_mocking.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'
