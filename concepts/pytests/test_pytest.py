"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

# Run test by keyword or substring in test name
$ pytest -k great -v

# Mark test to run
@pytest.mark.<markername>

$ pytest -m <markername> -v




Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories. Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them.

Pytest requires the test function names to start with test. Function names which are not of format test* are not considered as test functions by pytest. We cannot explicitly make pytest consider any function not starting with test as a test function.


"""
def test_greater():
    num = 100
    assert num > 100

def test_greater_equal():
    num = 100
    assert num >= 100

def test_less():
    num = 100
    assert num < 200

