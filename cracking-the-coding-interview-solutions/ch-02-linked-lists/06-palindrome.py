# Determine whether or not a linked list is a palindrome.

import unittest

def sol1(h):
  f,r = h,h
  r = reverse_copy(h)

  while f and r:
    if f.data != r.data:
      return False
    f,r = r.next, r.next
  return True

def _rev(c,p):
  if c:
    return
  n = copy(c.next)
  c.next = p
  _rev(n,p)


def reverse_copy(h):
  p = None
  c = copy(h)
  while c:
    n = c.next
    c.next = p
    p = c
    c = copy(n)
  return p


def copy(node):
  if node:
    return Node(node.data, node.next)
  else:
    return None

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(sol1(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(sol1(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(sol1(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(sol1(list4))
    
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(reverse_copy(head)), "40,30,20,10")

if __name__ == "__main__":
  unittest.main()

