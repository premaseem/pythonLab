"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol( head: ListNode) -> ListNode:
    "using stack "

    c = head
    arr = []
    while c:
        arr.append(c)
        c = c.next

    if not arr:
        return c
    c = arr.pop()
    nh = c
    while arr:
        c.next = arr.pop()
        c = c.next
    c.next = None
    return nh


def sol2(self, head: ListNode) -> ListNode:

        arr = []
        c = head
        while c:
            arr.append(c)
            c = c.next
        if not arr:
            return head

        arr.reverse()
        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        arr[-1].next=None
        return arr[0]

def sol3( head: ListNode) -> ListNode:
    p = None
    c = head
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    return p