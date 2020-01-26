# Determine whether or not one string is a permutation of another.

def sol1(s1,s2):
  return sorted(s1) == sorted(s2)


def load(s):
  d = {}
  for c in s:
    if d.get(c):
      d[c] = d.get(c)+1
    else:
      d[c] = 1
  return d

def sol2(s1, s2):
  d1,d2 = load(s1), load(s2)
  return d1 == d2


def sol3(str1, str2):
  counter = Counter()
  for letter in str1:
    counter[letter] += 1
  for letter in str2:
    if not letter in counter:
      return False
    counter[letter] -= 1
    if counter[letter] == 0:
      del counter[letter]
  return len(counter) == 0

class Counter(dict):
  def __missing__(self, key):
    return 0

print(f"The result is {sol1('aseem','seema')}")
print(f"The result is {sol1('jain','hain')}")

print(f"The result is {sol2('aseem','seema')}")
print(f"The result is {sol2('jain','hain')}")

print(f"The result is {sol3('aseem','seema')}")
print(f"The result is {sol3('jain','hain')}")


