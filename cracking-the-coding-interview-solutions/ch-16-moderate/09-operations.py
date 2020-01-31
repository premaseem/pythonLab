# Implement operations with only addition (and negation).

def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    diff = abs(a)
    p = 0
    for _ in range(abs(b)):
        p += diff

    if int(a < 0) + int( b < 0) == 1:
        return p
    return -p

def divide(a, b):
    if b == 0:
        return None
    q = 0
    diff = abs(b)
    p = 0
    while p < abs(a):
        p = p + diff
        q += 1
    if p > a:
        q -=1
    if int(a < 0) + int( b < 0) == 1:
        return q
    return -q


def subtract(a, b):
    diff = 0
    if (b < a):
      while b < a:
          diff += 1
          b += 1
      return diff

    else:
      while b > a:
          diff += 1
          a += 1
      return -diff


import unittest


class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(-8, 10), -80)
        self.assertEqual(multiply(3, 6), 18)
        self.assertEqual(multiply(7, 11), 77)

    def test_divide(self):
        self.assertEqual(divide(3, 6), 0)
        self.assertEqual(divide(30, 6), 5)
        self.assertEqual(divide(34, -6), -5)
        self.assertEqual(divide(120, 10), 12)

    def test_subtract(self):
        self.assertEqual(subtract(34, 6), 28)
        self.assertEqual(subtract(6, 10), -4)
        self.assertEqual(subtract(31, -6), 37)


if __name__ == "__main__":
    unittest.main()
