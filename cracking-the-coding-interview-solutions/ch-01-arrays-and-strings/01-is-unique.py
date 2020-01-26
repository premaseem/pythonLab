# Determine whether or not a given string contains no duplicate characters.

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


print(f"The result is {sol1('aseem')}")
print(f"The result is {sol1('jain')}")

print(f"The result is {sol2('ases')}")
print(f"The result is {sol2('jain')}")

print(f"The result is {sol3('aseem')}")
print(f"The result is {sol3('jain')}")

print(f"The result is {sol4('aseem')}")
print(f"The result is {sol4('jain')}")