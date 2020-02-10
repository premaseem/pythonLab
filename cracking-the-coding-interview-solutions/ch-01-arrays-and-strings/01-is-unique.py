# Determine whether or not a given string contains no duplicate characters.

import unittest

def sol1(s):
  return len(s) == len(set(s))

def sol2(s):
  for i,c in enumerate(s):
     if c in s[i+1:]:
       return False
  return True

def sol3(s):
  d = {}
  for c in s:
    if d.get(c):
      return False
    else:
      d[c]=True
  return True

def sol4(s):

  for x,c in enumerate(s):
    for y in range(x+1,len(s)):
      if c == s[y]:
        return False
  return True

def sol5(s):
  s = list(s)
  while s:
    if s.pop() in s:
        return False
  return True

class Test(unittest.TestCase):
  def test(self):

    self.assertFalse(sol5('aseem'))
    self.assertTrue(sol5('jain'))

    self.assertFalse(sol1('aseem'))
    self.assertTrue(sol1('jain'))

    self.assertFalse(sol2('aseem'))
    self.assertTrue(sol2('jain'))

    self.assertFalse(sol3('aseem'))
    self.assertTrue(sol3('jain'))

    self.assertFalse(sol4('aseem'))
    self.assertTrue(sol4('jain'))


if __name__ == "__main__":
  unittest.main()