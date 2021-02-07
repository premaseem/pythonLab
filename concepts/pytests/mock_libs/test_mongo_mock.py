"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

pip install mongoengine
pip install mongomock



"""

import unittest
from mongoengine import connect, disconnect, Document, StringField


class Person(Document):
    name = StringField()

class TestPerson(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def teardown_class(cls):
        """set up Db
        """
        print("class tear down")
        disconnect()

    def teardown_method(self,method):
        print("method  tear method ")

    def test_thing(self):
        pers = Person(name='John')
        pers.save()

        fresh_pers = Person.objects().first()
        assert fresh_pers.name ==  'John'

    def test_thing1(self):
        pers = Person(name='John')
        pers.save()

        fresh_pers = Person.objects().first()
        assert fresh_pers.name ==  'John'