"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
@classmethod
def setup_class(cls):
    """setup any state specific to the execution of the given class (which
    usually contains tests).
    """
    print("setup ")


@classmethod
def teardown_class(cls):
    """teardown any state that was previously setup with a call to
    setup_class.
    """
    print("tear down")

def test_my():
    print("pass")

test_my()