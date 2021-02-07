"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

# test_parameterized_fixture2.py
import pytest

class MyTester:
    def __init__(self, x):
        self.x = x

    def dothis(self):
        print(self)

@pytest.fixture
def tester(tester_arg):
    """Create tester object"""
    return MyTester(tester_arg)

def prod_bool(x):
    if x == 1:
        return True
    return False

class TestIt:
    # @pytest.mark.parametrize('tester_arg', [True, False])
    # def test_tc1(self, tester):
    #     tester.dothis()
    #     assert 1

    @pytest.mark.parametrize('arg,output', [(1,True), (0,False)])
    def test_tc2(self,arg,output):
        if arg:
            # self.assertTrue(prod_bool(arg))
            assert prod_bool(arg)
        else:
            assert not prod_bool(arg)
        

