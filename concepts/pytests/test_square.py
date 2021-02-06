"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

pytest grouping with mark or tag  
"""


import math
import pytest

@pytest.mark.sqr
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.equal
def test_equality():
    assert 10 == 11

@pytest.mark.sqr
def testsquare():
    num = 7
    assert 7*7 == 40

