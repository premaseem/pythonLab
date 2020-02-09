# Group string anagrams together.

def get_anagram(i,a):
  a1 = sorted(a[i])
  for x in range(i+1,len(a)):
    ag = sorted(a[x]) if a[x] else None

    if a1 == ag:
      ag = a[x]
      a[x] = None
      return "".join(ag)
  return None

def sol_1(a):
  final = []
  sa = []
  for i in range(len(a)):
    if (a[i]):
      ana = get_anagram(i,a)
      t = (a[i], ana)
      sa.append(t)
  print(sa)

  for t in sa:
    final.append(t[0])
    final.append(t[1])
  return final

def group_anagrams(strings):
  pairs = [(s, sorted(s)) for s in strings]
  pairs.sort(key=lambda p: p[1])
  return [p[0] for p in pairs]

import unittest

class Test(unittest.TestCase):
  def test_group_anagrams(self):
    strings = ["cat", "bat", "rat", "arts", "tab", "tar", "cat", "star"]
    self.assertEqual(sol_1(strings),
              ['cat', 'cat', 'bat', 'tab', 'rat', 'tar', 'arts', 'star'])
    strings = ["cat", "bat", "rat", "arts", "tab", "tar", "cat", "star"]
    self.assertEqual(group_anagrams(strings),
              ["bat", "tab", "cat", "cat", "arts", "star", "rat", "tar"])

if __name__ == "__main__":
  unittest.main()

