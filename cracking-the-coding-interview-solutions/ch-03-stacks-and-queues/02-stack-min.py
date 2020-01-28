#Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop and min should all operate in 0(1) time.

# Implement a stack with a function that returns the current minimum item.

class MinStack():
  def __init__(self):
    self.top, self._min = None, None

  def push(self,e):
    if self._min and (self._min.data < e):
      self._min = Node(self._min.data, self._min)
    else:
      self._min = Node(e, self._min)
    self.top = Node(e, self.top)

  def pop(self):
    if self.top:
      d = self.top.data
      self._min = self._min.next
      self.top = self.top.next
      return d

  def min(self):
    if not self._min:
      return None
    return self._min.data


class Node():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.min(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.min(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.min(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.min(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)

if __name__ == "__main__":
  unittest.main()

