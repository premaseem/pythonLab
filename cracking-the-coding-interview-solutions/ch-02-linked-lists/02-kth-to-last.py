# Return the k^{th} to last node in a linked list.

import unittest

# measuring the linked list length and return element
def sol1(head, k):
  c = head
  l =0
  while c is not None:
    l += 1
    c = c.next
  target = l -k
  c= head

  if (target < 0):
    return None

  for _ in range(target):
    c = c.next
  return c

# by lead and follow pattern
def sol2(head,k):
  lead,kth = head,head

  for _ in range(k):
    if lead is None:
      return None
    lead = lead.next

  while lead is not None:
    lead = lead.next
    kth = kth.next

  return kth

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, sol1(head, 0));
    self.assertEqual(7, sol1(head, 1).data);
    self.assertEqual(4, sol1(head, 4).data);
    self.assertEqual(2, sol1(head, 6).data);
    self.assertEqual(1, sol1(head, 7).data);
    self.assertEqual(None, sol1(head, 8));

    self.assertEqual(None, sol2(head, 0));
    self.assertEqual(7, sol2(head, 1).data);
    self.assertEqual(4, sol2(head, 4).data);
    self.assertEqual(2, sol2(head, 6).data);
    self.assertEqual(1, sol2(head, 7).data);
    self.assertEqual(None, sol2(head, 8));

if __name__ == "__main__":
  unittest.main()
