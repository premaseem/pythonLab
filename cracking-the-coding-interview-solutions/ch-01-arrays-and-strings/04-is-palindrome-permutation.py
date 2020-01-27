# Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.

def sol1(s):
  sr = s[::-1]
  return s == sr

def sol2(s):
  c = len(s) // 2
  p1 = s[:c]

  if c % 2 == 0:
    p2 = s[c+1:]
  else:
    p2 = s[c:]

  return  p1==p2[::-1]

def sol3(s):
  for i,c in enumerate(s):
    if c != s[len(s)-1-i]:
      return False
    # to optimize break it when its half loop
    if i == len(s)//2:
      break

  return True

def sol4(string):
  counter = Counter()
  for letter in string.replace(" ", ""):
    counter[letter] += 1
  #return sum([count % 2 for count in counter.values()]) < 2
  odd_counts = 0
  for count in counter.values():
    odd_counts += count % 2
    if odd_counts > 1:
      return False
  return True

class Counter(dict):
  def __missing__(self, key):
    return 0




print(f"The result is {sol1('aseesa')}")
print(f"The result is {sol1('asesa')}")
print(f"The result is {sol1('negativetest')}")

print(f"The result is {sol2('aseesa')}")
print(f"The result is {sol2('asesa')}")
print(f"The result is {sol2('negativetest')}")

print(f"The result is {sol3('aseesa')}")
print(f"The result is {sol3('asesa')}")
print(f"The result is {sol3('negativetest')}")

print(f"The result is {sol4('aseesa')}")
print(f"The result is {sol4('asesa')}")
print(f"The result is {sol4('negativetest')}")
print(f"The result is {sol4('fun nuf')}")



