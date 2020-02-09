# count linked list lenght in iterative way and recursive way

class Node:
    def __init__(self, d, n=None):
        self.d = d
        self.n = n

    def __str__(self):
        return str(self and self.d) + ", " + str(self.n and self.n)


class ll:
    def __init__(self):
        self.head = None

    def add(self, d):
        if not self.head:
            self.head = Node(d)
            return

        self.head = Node(d, self.head)

    def len_itr(self):
        cn = self.head
        count = 0
        while cn:
            count += 1
            cn = cn.n
        return count

    def len_rec(self, node, cnt=0):
        if not node:
            return cnt
        cnt += 1
        node = node.n
        return self.len_rec(node, cnt)

    def len_rec_1(self,node):
        if not node:
            return 0
        return 1 + self.len_rec_1(node.n )


o = ll()
o.add(1)
o.add(2)
o.add(3)
o.add(4)

print(o.head)
assert 4 == o.len_itr()
assert 4 == o.len_rec(o.head)
assert 4 == o.len_rec_1(o.head)
