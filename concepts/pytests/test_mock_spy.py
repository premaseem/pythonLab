"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

mocker.spy for Tracking Your Methods / or intercation
Sometimes you just want to keep track of a function’s usage in your application or codebase.

pip install pytest-mock
"""
class App:
    def call_db(self,emp_id):
        return emp_id * 1000

    ## production code ##
    def get_emp_salary(self,emp_id):
        print("called prod method")
        # connect mongoDb
        data = self.call_db(emp_id)
        return data
        # return emp_id * 1000

## production code ##


def test_get_emp_salary(mocker):
    o = App()
    spy = mocker.spy(App,'call_db')
    # mocker.patch("test_mocking_spy.get_emp_salary")
    o.get_emp_salary(10)
    o.call_db.call_count == 1
