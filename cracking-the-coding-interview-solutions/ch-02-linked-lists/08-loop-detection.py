# Detect whether or not a linked list contains a cycle.

import unittest

def sol1(h):
  s = set()
  while h:
    h = h.next
    if h in s:
      return h
    s.add(h)
  return False


# Detects the cyclic linked list, but does not return the starting node
def sol2(h):
  slow, fast = h,h
  while fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow :
      return True
  return False

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_detect_cycle(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertFalse(sol1(head1))
    self.assertFalse(sol2(head1))
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(sol1(head2), node1)
    self.assertTrue(sol2(head2))

if __name__ == "__main__":
  unittest.main()
