class Node:
    def __init__(self,d,p=None,n=None):
        self.prev = p
        self.data = d
        self.next = n

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        nn = Node(data)
        if not self.head:
            self.head = nn
            self.tail = nn
            return
        tn = self.tail
        tn.next = nn
        nn.prev = tn
        self.tail = nn

    def preprend(self,data):
        nn = Node(data)
        if not self.head:
            self.head = nn
            self.tail = nn
            return

        c = self.head
        nn.next = self.head
        c.prev = nn
        self.head = nn
        
    def add_after(self,k,data):
        nn = Node(data)
        c = self.head 
        while c.next: 
            if c.data == k:
                nn.next = c.next
                nn.prev = c
                c.next.prev = nn 
                c.next = nn
                return 
            c = c.next

        if c == self.tail:
            c.next = nn
            nn.prev = c
            self.tail = nn

    def add_before(self,k,data):
        nn = Node(data)
        if self.head.data == k:
            self.head.prev = nn
            nn.next = self.head
            self.head = nn
            return

        c = self.tail

        while c.prev:
            if c.data == k:
                nn.next = c
                nn.prev = c.prev

                c.prev.next = nn
                c.prev = nn
                return
            c = c.prev

        
                
                
            

    def print(self):
        c = self.head
        while c:
            print(c.data, " - ",end="")
            c = c.next

    def print_rev(self):
        print("\n reverse print")
        c = self.tail
        while c:
            print(c.data, " - ",end="")
            c = c.prev



dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)

# dll.add_after(3,"a")
dll.add_before(1,"z")
dll.print()
dll.print_rev()





