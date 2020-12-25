class n:
    def __init__(s,v):
        s.v = v
        s.l = None
        s.r = None


class bst:
    def __init__(self,v):
        # if not self.root:
        self.root = n(v)

    def ins(self, v, node):
        if not node:
            return n(v)
        if v < node.v:
            node.l = self.ins(v, node.l)
        else:
            node.r = self.ins(v, node.r)
        return node

    def _print(self,n,s):
        if not n:
            return ""
        s += str(n.v) + "-"

        if n.l:
            s = self._print(n.l,s)
        if n.r:
            s = self._print(n.r,s)

        return s

    def print(self):
        print(self._print(self.root,""))

    def insert(self,v):
        self.ins(v,self.root)

    def _search(self,n,v):
        if not n:
            return False
        if n.v == v:
            return True
        elif  v < n.v:
            return self._search(n.l,v)
        else:
            return self._search(n.r,v)
    def search(self,v):
        print(v, "does exists in tree? ",self._search(self.root,v))

    def _sat(self,node,f):
        if node.l:
            if node.v < node.l.v:
                return False
        if node.r:
            if node.v > node.r.v:
                return False

        if node.l:
            f= self._sat(node.l,f)
        if node.r:
            f= self._sat(node.r,f)

        if f:
            return True
        return False

    def is_bst_satisfied(self):
        print(self._sat(self.root,True))




t = bst(50)
t.insert(40)
t.insert(60)
t.insert(45)
t.insert(65)
t.insert(55)
t.insert(55)
# t.root.r.v=2

t.print()
t.search(100)
t.search(45)
t.is_bst_satisfied()