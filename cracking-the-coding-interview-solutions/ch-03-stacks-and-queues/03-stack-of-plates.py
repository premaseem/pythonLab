# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP

# Implement a class that acts as a single stack made out of multiple stacks
# which each have a set capacity.

class MultiStack():
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = []

  def push(self, e):
    if len(self.stacks) and (len(self.stacks[-1]) < self.capacity):
      self.stacks[-1].append(e)
    else:
      self.stacks.append([e])

  # def pop(self):

  def pop(self):
    while len(self.stacks) and (len(self.stacks[-1]) == 0):
      self.stacks.pop()
    if len(self.stacks) == 0:
      return None
    item = self.stacks[-1].pop()
    if len(self.stacks[-1]) == 0:
      self.stacks.pop()
    return item

  def pop_at(self, i):
    if len(self.stacks) < i or (i < 0):
      return None
    if len(self.stacks[i]) == 0:
      return
    return self.stacks[i].pop()

import unittest

class Test(unittest.TestCase):
  def test_multi_stack(self):
    stack = MultiStack(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
    self.assertEqual(stack.pop_at(1), 66)
    self.assertEqual(stack.pop_at(0), 33)
    self.assertEqual(stack.pop_at(1), 55)
    self.assertEqual(stack.pop_at(1), 44)
    self.assertEqual(stack.pop_at(1), None)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 77)
    self.assertEqual(stack.pop(), 22)
    self.assertEqual(stack.pop(), 11)
    self.assertEqual(stack.pop(), None)

if __name__ == "__main__":
  unittest.main()

