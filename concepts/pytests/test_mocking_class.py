"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

from time import sleep

class Applicaton:
    def is_windows(self):
            # This sleep could be some complex operation instead
            sleep(1)
            return True

    def get_operating_system(self):
            return 'Windows' if self.is_windows() else 'Linux'


# 'mocker' fixture provided by pytest-mock
def test_get_operating_system(mocker):
    app_obj = Applicaton()
    # Mock the slow function and return True always
    mocker.patch('test_mocking_class.Applicaton.is_windows', return_value=True)
    assert app_obj.get_operating_system() == 'Windows'
