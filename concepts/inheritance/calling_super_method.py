# Objective is to invoke base method super class from derived class
# @Author Aseem Jain

class Base(object):
    def base_method(self):
        print("This is base method providing credentials")

class Sub(Base):
    def get_db_credetials(self):
        super().base_method()

s = Sub()
s.get_db_credetials()

