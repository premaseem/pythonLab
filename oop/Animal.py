__author__ = 'asee2278'

class Animal(object) :

    def __init__(self):
        self.name = "kallu kutta"



    def eat(self):
        name = "most sexy"
        print name + "is eating"
        return self.name


kallu = Animal()
print kallu.eat();


class Shape :
    name="var"
    def __init__(self,name):
        self.name = "circle"

    # print "This is shape is {}".format(name)
    shape = "circle"
    def print_shape(self):
        print self.shape;

gola = Shape("cirlce")