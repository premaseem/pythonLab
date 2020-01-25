__author__ = 'asee2278'

class circle(object) :
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        pass

    def area(self):
        return self.radius ** 2 * self.pi

    def set_radius(self,radius):
        self.radius = radius;
        print self.radius
        return self.radius


c = circle(2)
c.set_radius(100)
print c.area()
print c.radius
lund = circle(3).set_radius(1)
lund(6)
