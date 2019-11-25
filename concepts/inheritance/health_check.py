from abc import ABC, abstractmethod

class Base(object):
    def invoker(self):
        print("boiler place")
        self.abs_method()

    def abs_method(self):
        print("base abs mthod")

class Sub(Base):
    def abs_method(self):
        print("product specific base method")

# b = Base()
# b.invoker()

s = Sub()
s.invoker()