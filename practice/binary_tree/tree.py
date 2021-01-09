# Binary Tree

class Node:
    def __init__(self,v):
        self.v = v
        self.l = None
        self.r = None

class BT:
    def __init__(self,v):
        self.root = Node(v)


    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.v) + "-")
            traversal = self.preorder_print(start.l, traversal)
            traversal = self.preorder_print(start.r, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """->Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.l, traversal)
            traversal = self.postorder_print(start.r, traversal)
            traversal += (str(start.v) + "-")
        return traversal

    def breadth_first_print(self, node):
        """Root->Left->Right"""
        if not node:
            return

        q = MyQueue()
        q.enqueue(node)
        ans = ""

        while not q.isEmpty():
            n = q.dequeue()
            ans += str(n.v) + "-"

            if n.l:
                q.enqueue(n.l)
            if n.r:
                q.enqueue(n.r)

        return ans

    def pre(self):
        print("pre order ---->  ")
        print(self.preorder_print(self.root,""))

    def inorder(self):
        print("breadth first order ---->  ")
        print(self.breadth_first_print(self.root))

class MyQueue:
    def __init__(self):
        self.arr = []

    def enqueue(self,n):
        self.arr.insert(0,n)

    def dequeue(self):
        if not self.isEmpty() :
            return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        return self.arr[-1]

# Populate the binary tree
tree = BT(10)
tree.root.l = Node(11)
tree.root.l.l = Node(22)
tree.root.l.r = Node(23)
tree.root.r = Node(12)
tree.root.r.l = Node(23)
tree.root.r.r = Node(24)

# print pre order ( depth first )
# tree.pre()

# print in order ( depth first )
# tree.post()

# print post order ( depth first )
tree.inorder()







