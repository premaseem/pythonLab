# Sum two numbers that are represented with linked lists with decimal digits
# in reverse order of magnitude.

import unittest

def sol1(h1,h2):

  h3 = Node(0)
  t = h3
  carry = 0
  while h1 is not None:
    a = h1.data + h2.data + carry
    if a - 10 > 0:
      carry = a - 10
      h3.next = Node(a//10)
    else:
      carry = 0
      h3.next = Node(a)
    h1,h2,h3 = h1.next,h2.next,h3.next

  return t.next

def sol2(num1, num2):
  node1, node2 = num1, num2
  carry = 0
  result_head, result_node = None, None
  while node1 or node2 or carry:
    value = carry
    if node1:
      value += node1.data
      node1 = node1.next
    if node2:
      value += node2.data
      node2 = node2.next
    if result_node:
      result_node.next = Node(value % 10)
      result_node = result_node.next
    else:
      result_node = Node(value % 10)
      result_head = result_node
    carry = value / 10
  return result_head

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string
    
class Test(unittest.TestCase):
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sol1(num1, num2)), "5,1,9")


if __name__ == "__main__":
  unittest.main()

