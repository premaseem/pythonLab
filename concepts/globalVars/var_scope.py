my_var = "global level"

class MyClass:
    my_var = "class level"

    def __init__(self,val):
        self.my_var = val

    def set_var(self, val):
        global my_var
        my_var = val

    def get_var(self):
        # my_var = "local"
        global my_var
        return my_var

    def func(self):
        for i in range(5):
            print(i)



def method():
    global my_var
    my_var = "prem"
    print(my_var)

# method()
# print(MyClass.my_var)
obj = MyClass("instance level")
obj.set_var("global")
# print(my_var)
print(obj.get_var())

