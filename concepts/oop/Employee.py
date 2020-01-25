__author__ = 'asee2278'


class Person:
    nameP = "Aseem"
    def shit(self):
        print "normal potty"
    pass



class Employee(Person):
   'Common base class for all employees'
   empCount = 0

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
      #super(Person,self).shit(self)

#   def shit(self):
#       print "dollar potty"

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1


obj =Employee("prem mongo",6000,)
print obj.displayEmployee()
obj.shit()
obj.dickSize = 12
"""
print obj.dickSize
print hasattr(obj,"dickSize")
print delattr(obj,"dickSize")
print hasattr(obj,"dickSize")
print obj.__dict__
print obj.__module__
print obj.__module__
"""