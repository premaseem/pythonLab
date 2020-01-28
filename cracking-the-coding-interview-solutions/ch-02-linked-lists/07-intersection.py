# Return an intersecting node if two linked lists intersect.

import unittest

def sol1(h1,h2):
  s = set()
  while h1:
    s.add(h1)
    h1 = h1.next

  while h2:
    if h2 in s:
      return h2
    h2 = h2.next

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(sol1(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(sol1(head3, head4), node)

if __name__ == "__main__":
  unittest.main()

