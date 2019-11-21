_cluster = None

class Human():
    def talk(self):
        if _cluster is None:
            print("human talking")
        else:
            print ("human esp called")

    def walk(self):
        print("human walking")

class Man():
    def talk(self):
        if _cluster is None:
            print("Man talking")
        else:
            _cluster.talk()

class Woman:
    def talk(self):
        print("Woman talking")
    def setCluster(self,cluster):
        global _cluster
        _cluster = cluster


objbase = Human()
objspe = Man()

obj = Woman()
obj.setCluster(objbase)

objspe.talk()
# objspe.walk()

