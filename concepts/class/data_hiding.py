class Car:
    def __init__(self):
        self.__speed = "Initialized"
        self.myspeed = "123"

    def set_speed(self,x):
        self.__speed = x

    def get_speed(self):
        return self.__speed

obj = Car()
obj.set_speed(100)


print(obj.get_speed())

print(dir(obj))
print(obj.__dict__)

# Cannot access the private variable in object, its hiddern with __
print(obj.__speed)
