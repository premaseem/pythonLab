import concepts.enum.my_enums as myenum

class Main(object):

    def printenum(self):
        print(myenum.NodeStatus.healthy.value)
        print(myenum.NodeStatus.bootstrap.value)

Main().printenum()