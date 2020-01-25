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
        else:
            o.next = self.head
            self.head = o

    def add_last(self, data):
        o = N(data)
        if self.head is None:
            self.head = o
        else:
            c = self.head
            while c.next is not None:
                c = c.next
            c.next = o

    def search_data(self,num):
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

    def pretty_print(self):
        c = self.head
        while c is not None:
            print(c.data, end= " -> ")
            c = c.next
        print("None")

ll_data = [i for i in range(10) if i%2==0]
myll = MyLinedlist()
for d in ll_data:
    # myll.add_last(d)
    myll.add_last(d)
myll.pretty_print()
print(myll.search_data(2))
print(myll.delete_data(3))
print(myll.delete_data(4))
