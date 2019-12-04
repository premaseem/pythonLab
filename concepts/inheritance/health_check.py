from abc import ABC, abstractmethod

class Base(object):
    def invoker(self):
        print("boiler place")
        self.abs_method()

    def abs_method(self):
        print("base abs mthod")

    def get_db_credentials(self):
        print("getting the db creds")

class Sub(Base):
    def abs_method(self):
        print("product specific base method")
        super().get_db_credentials()


# b = Base()
# b.invoker()

s = Sub()
s.invoker()
s.abs_method()