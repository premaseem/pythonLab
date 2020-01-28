# Remove the duplicate values from a linked list.

import unittest

def sol1(h):
  c = h
  s = set()
  s.add(h.data)
  while c.next is not None:
     if c.next.data in s:
       c.next = c.next.next
     else:
        s.add(c.next.data)
        c = c.next

def is_dup(h, data):
  node = h
  c = 0
  while  node is not None:
    if data == node.data:
      c += 1
    node = node.next
  return c > 1

# Without using the buffer
def sol2(h):
  c = h
  while c.next is not None:
    if is_dup(h,c.next.data):
      c.next = c.next.next
    else:
      c = c.next


class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    sol1(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    sol2(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
  unittest.main()

