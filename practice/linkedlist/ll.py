class n:
    def __init__(self,v):
        self.v=v
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,v):
        nn = n(v)
        if not self.head:
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn

    def append(self,v):
        cn = self.head
        
        while cn.next:
            cn = cn.next
        cn.next = n(v)

    def print(self):
        print()
        nn = self.head
        while nn:
            print(nn.v,end="-")
            nn = nn.next

    def delete(self,v):

        if self.head.v == v:
            self.head = self.head.next
            return

        pn = self.head
        cn = pn.next
        while cn:
            if cn.v == v:
                pn.next = cn.next
            pn = cn
            cn = cn.next
            
    def delete_by_position(self, i):
        if i == 0:
            self.head = self.head.next
            return

        pn = self.head 
        cn = self.head.next
        position = 1
        while cn: 
            if position == i:
                pn.next = cn.next
                return 
            pn = cn 
            cn = cn.next
            position += 1 
        
    def size_itr(self):
        n = self.head
        size = 0
        while n:
            size += 1
            n = n.next
        print("\nsize is")
        print(size)
        return size
    
    def size_rec(self,n):
        if not n:
            return 0
        return 1 + self.size_rec(n.next)

    def swap1(self,k1,k2):
        cn = self.head
        while cn: 
            if cn.v == k1:
                cn.v =  float('inf')
            if cn.v == k2:
                cn.v = k1
            cn = cn.next

        cn = self.head
        while cn:
            if cn.v == float('inf'):
                cn.v = k2
            cn = cn.next

    def swap2(self,k1,k2):
        cn = self.head
        p1 = 0
        p2 = 0
        i = 0
        while cn:
            if cn.v == k1:
                p1 = i
            if cn.v == k2:
                p2 = i
            cn = cn.next
            i += 1

        cn = self.head

        j=0
        while cn:
            if j == p1:
                cn.v = k2
            if j == p2:
                cn.v = k1
            cn = cn.next
            j += 1

    def swap3(self,k1,k2):
        p1 = p2 = None
        pn = self.head
        cn = self.head.next
        if pn.v == k1 or pn.v == k2:
            p1 = pn

        while cn:
            if cn.v == k1:
                p1 = pn
            if cn.v == k2:
                p2 = pn
            pn = cn
            cn = cn.next

        p1.next, p2.next = p2.next,p1.next
        p1.next.next, p2.next.next = p2.next.next,p1.next.next

    def reverse(self):
        pn = None
        cn = self.head
        while cn:
            nxt = cn.next
            cn.next = pn
            pn = cn
            cn = nxt
        self.head = pn
        self.print()


    def reverse_stack(self):
        stk = []
        cn = self.head
        while cn:
            stk.append(cn)
            cn = cn.next

        self.head = stk.pop()
        cn = self.head
        while len(stk) > 0 and cn:
            cn.next = stk.pop()
            cn = cn.next
        cn.next = None
        self.print()

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def sort_merge(self,l1,l2):
        c1 = l1.head
        c2 = l2.head
        new_head = None
        if c1.v <= c2.v:
            new_head = c1
            c1 = c1.next
        else:
            new_head = c2
            c2 = c2.next
        p = new_head
        while c1 and c2:
            if c1.v <= c2.v:
                p.next = c1

                c1 = c1.next
            else :
                p.next = c2
                # p = c2
                c2 = c2.next
            p= p.next

        if c1:
            p.next = c1
        if c2:
            p.next = c2

        print("merged list")
        nn = new_head
        while nn:
            print(nn.v,end="-")
            nn = nn.next

    def remove_dup(self):
        m = {}
        c = self.head
        while c:
            v = c.v
            if not m.get(v):
                m[v] = 1
            else:
                p = m.get(v)
                p += 1
                m[v] = p
            c = c.next

        print(m)
        self.print()
        prev = self.head
        curr = self.head.next
        while curr:
            v = curr.v
            p = m.get(v)
            if p != 1:
                prev.next = curr.next
                p -= 1
                m[v] = p
            else:
                prev = curr
            curr = curr.next
        # self.print()

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.v in dup_values:
                # Remove node:
                prev.next = cur.next
            else:
                # Have not encountered element before.
                dup_values[cur.v] = 1
                prev = cur
            cur = prev.next

    # 2 pointer approach
    def get_n_from_last(self,n):
        front = self.head
        back = self.head
        for i in range(n):
            front = front.next

        while back and front:
            back = back.next
            front = front.next

        return back.v

    def count(self,data):
        def count_data(data, n):
            if not n:
                return 0
            if data == n.v:
                return  1 + count_data(data,n.next)
            else:
                return count_data(data,n.next)

        num = count_data(data,self.head)
        print("count of ", data, "is ", num)
        return num

    def rotate(self, k):
        if self.head.v == k:
            return
        break_node = None
        curr = self.head
        prev = None
        while curr.next:
            if curr.v == k:
                break_node = curr
                prev.next = None
            prev = curr
            curr = curr.next

        curr.next = self.head
        self.head = break_node
        # prev.next = None
        # se

    def is_palendrome(self):
        c = self.head
        l = 0
        n = []

        while c:
            l += 1
            n.append(c)
            c = c.next

        sp = self.head

        for i in range((l//2)):
            if sp.v != n.pop().v :
                return False
            sp = sp.next
        return True

    def tail_to_head(self):
        c = self.head
        p = None
        while c.next:
            p = c
            c = c.next
        p.next = None
        c.next = self.head
        self.head = c
        print("moved head ")
        self.print()

    def sum(self,l1,l2):

        p = l1.head
        q = l2.head
        ans = n(0)
        ans_head = ans
        c=0
        d=0
        while p and q:
            s = p.v + q.v + c
            c = 0
            if s > 9 :
                d = s % 10
                c = 1
            else:
                d =s
            ans.next = n(d)
            ans = ans.next
            p = p.next
            q = q.next

        while p:
            ans.next = n(p.v + c)
            c = 0
            p = p.next
            ans = ans.next
        while q:
            ans.next = n(q.v + c)
            c=0
            q = q.next
            ans = ans.next


        print("sum of", l1.print())
        print("sum of", l2.print())
        while ans_head:
            print(ans_head.v)
            ans_head = ans_head.next





# ll = LinkedList()
# ll.add(10)
# ll.add(9)
# ll.add(8)
# ll.append(100)
# ll.print()
# ll.delete(9)
# ll.print()
# ll.delete_by_position(3)
# ll.print()
# ll.size_itr()
# print(ll.size_rec(ll.head))
# ll.add(110)
# ll.add(19)
# ll.add(18)
# ll.print()
# ll.swap3(18,100)
# ll.add(10)
# ll.add(20)
# ll.add(30)
# ll.add(40)
# ll.print()
# print("reverse")
# ll.reverse_recursive()
# # ll.reverse_stack()
# ll.print()


### Merge 2 linked lists ###

# l1 = LinkedList()
# l1.add(40)
# l1.add(30)
# l1.add(20)
# l1.add(10)
# l1.print()
#
# l2 = LinkedList()
# l2.add(45)
# l2.add(35)
# l2.add(25)
# l2.add(15)
# l2.print()
#
# l1.sort_merge(l1,l2)

### remove duplicates ###
l2 = LinkedList()
l2.add(10)
l2.add(20)
# l2.add(10)
# l2.add(15)
# l2.add(15)
# l2.add(15)
l2.add(15)
# l2.add(20)
l2.add(50)
l2.add(500)
l2.add(250)


l2.print()
# l2.remove_dup()
# l2.remove_duplicates()
print("nth last element : ",l2.get_n_from_last(2))
# l2.count(15)
lp = LinkedList()
lp.add("r")
lp.add("a")
lp.add("d")
lp.add("a")
lp.add("r")
print("is palendrome ",lp.is_palendrome())
lp.tail_to_head()
l2.rotate(250)
l2.print()

n1=  LinkedList()
n1.add(5)
n1.add(6)
n1.add(3)

n2=LinkedList()
n2.add(9)
n2.add(9)
# n2.add(2)
# n2.add(3)

n3=LinkedList()
n3.add(9)
n3.add(9)
n3.add(9)
n1.sum(n3, n2)


