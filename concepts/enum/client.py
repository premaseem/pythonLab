import concepts.enum.my_enums as myenum

class Main(object):

    def printenum(self):
        print(myenum.NodeStatus.healthy.value)
        print(myenum.NodeStatus.bootstrap.value)
        st = "healthy"
        return "labs-"+myenum.NodeStatus[st].value


Main().printenum()
print(Main().printenum())