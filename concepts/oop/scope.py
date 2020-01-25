
# @classmethod vs @staticmethod
class Foo(object):

    # you couldn't use self. or cls. out here, they wouldn't mean anything

    # this is a class attribute
    thing = 'athing'

    def __init__(self, bar):
        # I want other methods called on this instance of Foo
        # to have access to bar, so I create an attribute of self
        # pointing to it
        self.bar = bar

    @staticmethod
    def default_foo():
        # static methods are often used as alternate constructors,
        # since they don't need access to any part of the class
        # if the method doesn't have anything at all to do with the class
        # just use a module level function
        return Foo('baz')

    @classmethod
    def two_things(cls):
        # can access class attributes, like thing
        # but not instance attributes, like bar
        print cls.thing

    def normal(self):
        # global thing
        print self.thing, self.bar


# Foo.default_foo()
# Foo.two_things()
Foo.two_things()
Foo("v").normal()