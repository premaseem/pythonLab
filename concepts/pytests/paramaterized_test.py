"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Data driven testing without a need to duplication of test case
Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −
"""

import pytest

@pytest.mark.parametrize("input,output",[(1,11),(2,22),(3,33)])
def test_11_multiple(input,output):
    assert 11*input == output



