"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Abstract classes are classes that contain one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.

TypeError: Can't instantiate abstract class A with abstract methods forced_implementation
"""
from abc import ABC,abstractmethod

class MyBaseClass(ABC):
    """ Defines the interface or contract for all sub classes """

    @abstractmethod
    def forced_implementation(self,a,b):
        pass

class A(MyBaseClass):
    def forced_implementation(self):
        print("implemented in A ")

class B(MyBaseClass):
    pass

print(A().forced_implementation())

# Cannot instanciate object B
print(B().forced_implementation())

