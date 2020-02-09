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

    def swap(self, s1, s2):
        c = self.head
        p = None
        while c:
            if c.d == s1:
                break
            p = c
            c = c.n
        p1 = p
        c1 = c

        c = self.head
        p = None
        while c:
            if c.d == s2:
                break
            p = c
            c = c.n
        p2 = p
        c2 = c

        if not c1 or not c2:
            return

        if p1:
            p1.n = c2
        else:
            self.head = c2

        if p2:
            p2.n = c1
        else:
            self.head = c1

        c1.n, c2.n = c2.n, c1.n




o = ll()
o.add("A")
o.add("B")
o.add("C")
o.add("D")
o.add("E")

print(o.head)
assert 5 == o.len_itr()
assert 5 == o.len_rec(o.head)
assert 5 == o.len_rec_1(o.head)

# swap C and B
o.swap("A","E")
print(o.head)

