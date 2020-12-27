# CIRCULAR LINKED LIST
# the tail node points to the head of the linked list instead of pointing to null which makes the linked list circular.

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        # nn = Node(value)
        # self.head = nn
        # nn.next = nn

    def append(self,value):
        nn = Node(value)
        if not self.head:
            self.head = nn
            nn.next = nn
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = nn
        nn.next = self.head
        # self.head = nn

    def prepend(self,value):
        nn = Node(value)
        if not self.head:
            self.head = nn
            nn.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = nn

        nn.next = self.head
        self.head = nn

    def remove(self, value):

        # remove the head value
        if self.head.value == value:
            c = self.head
            while c.next != self.head:
                c = c.next
            c.next = self.head.next
            self.head = self.head.next
            return

        # remove any other value
        prev = None
        cur = self.head
        while cur.next != self.head :
            if cur.value == value:
                break
            prev = cur
            cur = cur.next

        prev.next = cur.next

    def __len__(self):
        if not self.head:
            return 0
        c = self.head
        cnt = 1
        while c.next != self.head:
            cnt += 1
            c = c.next
        print("\n size is:",cnt)
        return cnt

    def split_2_halfs(self):
        mid = len(self) // 2
        h1 = self.head
        for i in range(mid-1):
            h1 = h1.next
        l1 = h1

        h2 = h1.next
        print(h2.value)

        l2 = h2
        for i in range(mid-1):
            l2 = l2.next
        print(l2.value)

        # first ccl
        h1.next = self.head
        self.print()

        # second ccl
        l2.next = h2
        c = h2
        while c:
            print(c.value, " - ", end="")
            c = c.next
            if c == h2:
                break





        # h1 = self.head
        # for i in range(mid-1):
        #     h1 = h1.next
        #
        # h2 = h1
        # h1.next = self.head
        # c = h2.next
        # while c.next != self.head:
        #     c = c.next
        # c.next = h2.next
        #
        # # h1.next = self.head
        # cll2 = CLL()
        # cll2.head = h2.next
        # cll2.print2()
        # cur = cll2.head
        # while cur.next != cll2.head:
        #     print(cur.value)
        #     cur = cur.next
        # # self.print(cll2)
        #
        # self.print(self.head)






    def print(self,h = None):
        print()
        if h :
            h_v = h
            cur = h
        else :
            h_v = self.head
            cur = self.head if not h else h

        # print(self.head.value)
        while cur.next != h_v:
            print(cur.value,"-",end=" ")
            cur = cur.next
        print(cur.value)

    def print2(self):
        print()
        cur = self.head
        while cur:
            print(cur.value,end=" - ")
            cur = cur.next
            if cur == self.head:
                break



cll = CLL()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)
cll.append(6)

# cll.print2()
# cll.prepend(100)
# cll.remove(3)
cll.print2()
# len(cll)
cll.split_2_halfs()

