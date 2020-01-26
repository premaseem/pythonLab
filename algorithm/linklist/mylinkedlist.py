class N():
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, addr):
        self.next = addr


class MyLinedlist():
    head = None
    tail = None

    def add_first(self, data):
        o = N(data)
        if self.head is None:
            self.head = o
            self.tail = o
        else:
            o.next = self.head
            self.head = o

    def add_last(self, data):
        o = N(data)
        if self.head is None:
            self.head = o
            self.tail = o
        else:
            c = self.head
            while c.next is not None:
                c = c.next
            c.next = o
            self.tail = o

    def add_via_tail(self, data):
        o = N(data)
        if self.tail is None:
            self.tail = o
            self.head = o
        else:
            c = self.tail
            c.next = o
            self.tail = o

    def search_data(self, num):
        c = self.head
        while c is not None:
            if c.data == num:
                return "num found"
            c = c.next
        return "num not found"

    def delete_data(self, num):
        c = self.head
        if c.data == num:
            self.head = c.next
            self.pretty_print()
            return "deleted"

        while c.next is not None:
            if c.next.data == num:
                c.next = c.next.next
                self.pretty_print()
                return "deleted"
            c = c.next
        return "num not found: cannot delete"

    def delete_by_index(self, i):
        c = self.head
        if i == 0:
            self.head = c.next
            return "deleted"
        l = 0

        while c.next is not None:
            l += 1
            if l == i:
                c.next = c.next.next
                self.pretty_print()
                return "deleted"
            c = c.next
        return "out of index: cannot delete"

    def reverse(self):
        self._reverse(self.head, None)
        self.head, self.tail = self.tail, self.head

    def _reverse(self, c, p):
        if c is None:
            return
        n = c.next
        c.next = p
        self._reverse(n, c)

    def pretty_print(self):
        c = self.head
        s = ""
        while c is not None:
            s = s + str(c.data) + " -> "
            c = c.next
        s = "[ " + s[:-3] + "]"
        print(s)

    def pretty_print_tail(self):
        c = self.tail
        s = ""
        while c is not None:
            s = s + str(c.data) + " -> "
            c = c.next
        s = "[ " + s[:-3] + "]"
        print(s)


ll_data = [i for i in range(10) if i % 2 == 0]

# myll = MyLinedlist()
# for d in ll_data:
#     # myll.add_last(d)
#     myll.add_last(d)
# myll.pretty_print()
# print(myll.search_data(2))
# print(myll.delete_by_index(3))
# print(myll.delete_by_index(5))
# print(myll.delete_by_index(0))

# adding via tail
# myll = MyLinedlist()
# ll_data = [i for i in range(15) if i%3==0]
# myll.add_first(7)
# for d in ll_data:
#     myll.add_via_tail(d)
# myll.add_last(17)
#
# myll.pretty_print()
# myll.delete_by_index(3)

# reverse return linked list
myll = MyLinedlist()
ll_data = [i for i in range(50) if i % 5 == 0]

for d in ll_data:
    myll.add_via_tail(d)
myll.pretty_print()
myll.reverse()

myll.pretty_print()
