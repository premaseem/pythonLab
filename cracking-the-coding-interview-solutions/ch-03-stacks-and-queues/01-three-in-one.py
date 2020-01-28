# Use a single array to implement three stacks.

class ThreeStacks():
  def __init__(self):
    self.array = [None, None, None]
    self.current = [0,1, 2]
    self.sp1=0
    self.sp2=1
    self.sp3=2

# solution 1 : not very dynamic
  def _push(self, item, sn):

    h =max(self.sp1,self.sp2,self.sp3)

    while len(self.a) <= h:
      self.a.append(None)

    if sn == 1:
      self.a[self.sp1] = item
      self.sp1 += 3

    if sn == 2:
      self.a[self.sp2] = item
      self.sp2 += 3

    if sn == 3:
      self.a[self.sp3] = item
      self.sp3 += 3

# solution 1 : not very dynamic
  def _pop(self,sn):
      if sn == 1:

        if self.sp1-3 < 0:
          return
        self.sp1 -= 3
        item = self.a[self.sp1]
        self.a[self.sp1] = None

      if sn == 2:

        if self.sp2-3 < 0:
          return
        self.sp2 -= 3
        item = self.a[self.sp2]
        self.a[self.sp2] = None

      if sn == 3:
        if self.sp3-3 < 0:
          return
        self.sp3 -= 3
        item = self.a[self.sp3]
        self.a[self.sp3] = None

      return item



  def push(self, item, stack_number):
    stack_number -= 1
    while len(self.array) <= self.current[stack_number]:
      self.array += [None] * len(self.array)
    self.array[self.current[stack_number]] = item
    self.current[stack_number] += 3

  def pop(self, stack_number):
    stack_number -= 1
    if self.current[stack_number] > 3:
      self.current[stack_number] -= 3
    item = self.array[self.current[stack_number]]
    self.array[self.current[stack_number]] = None
    return item

import unittest

class Test(unittest.TestCase):
  def test_three_stacks(self):
    three_stacks = ThreeStacks()
    three_stacks.push(101, 1)
    three_stacks.push(102, 1)
    three_stacks.push(103, 1)
    three_stacks.push(201, 2)
    self.assertEqual(three_stacks.pop(1), 103)
    self.assertEqual(three_stacks.pop(2), 201)
    self.assertEqual(three_stacks.pop(2), None)
    self.assertEqual(three_stacks.pop(3), None)
    three_stacks.push(301, 3)
    three_stacks.push(302, 3)
    self.assertEqual(three_stacks.pop(3), 302)
    self.assertEqual(three_stacks.pop(3), 301)
    self.assertEqual(three_stacks.pop(3), None)

if __name__ == "__main__":
  unittest.main()
