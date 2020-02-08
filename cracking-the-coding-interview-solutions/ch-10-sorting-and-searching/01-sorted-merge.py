# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

# Merge array b into array a given that array a contains len(b) extra space at
# the end.

def sol1(a,b):
  bl = len(b)
  al = len(a) - bl
  x=1
  y=1

  for i in range(len(a) - 1, -1, -1):
    if b[bl-y] < a[al-x] and al-x >= 0:
      a[i] = a[al-x]
      x += 1
    else:
      a[i] = b[bl-y]
      y += 1
      if y > bl:
        break

  print(a)


import unittest

class Test(unittest.TestCase):
  def test_sorted_merge(self):
    a = [33, 44, 55, 66, 88, 99, None, None, None]
    b = [11, 22, 77]
    sol1(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 77, 88, 99])
    a = [11, 22, 55, 66, 88, None, None, None]
    b = [33, 44, 99]
    sol1(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 88, 99])

if __name__ == "__main__":
  unittest.main()

