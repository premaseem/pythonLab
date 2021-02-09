# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
# from sample.simple import add_one

from project.prescription_routing.src.app.app import Pharmacy


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.csv = Pharmacy("CVS")

    def test_inventory(self):
        print(self.csv)

    def test_inventory1(self):
        print(self.csv)






if __name__ == '__main__':
    unittest.main()
