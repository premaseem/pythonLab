class N:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        o = N(data)
        if self.root is None:
            self.root = o
            return
        self._insert(self.root, o)

    def _insert(self, c, o):
        if o.data < c.data:
            if c.l is None:
                c.l = o
                return
            else:
                self._insert(c.l, o)
        else:
            if c.r is None:
                c.r = o
                return
            else:
                self._insert(c.r, o)

    def search(self,data):
        return self._search(self.root,data)

    def _search(self,o, data):
        if o is None:
            return "Cannot find number"
        else:
            if data == o.data:
                return "got the number"
            if data < o.data:
                return self._search(o.l,data)
            else:
                return self._search(o.r, data)
        # return "Cannot find number"



    def in_order(self, c):
        if c is None:
            return
        self.in_order(c.l)
        print(c.data)
        self.in_order(c.r)

    def pre_order(self, c):
        if c is None:
            return
        print(c.data)
        self.in_order(c.l)
        self.in_order(c.r)

    def post_order(self, c):
        if c is None:
            return
        self.in_order(c.l)
        self.in_order(c.r)
        print(c.data)


bt = BST()
bt.insert(9)
bt.insert(81)
bt.insert(4)
bt.insert(11)
bt.insert(3)
bt.in_order(bt.root)
print(bt.search(4))
print(bt.search(41))
