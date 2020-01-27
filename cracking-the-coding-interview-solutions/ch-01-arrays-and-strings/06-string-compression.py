# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

def sol1(s):
  scope = s[0]
  s = s [1:]
  count = 1
  fs = ""

  for i,c in enumerate(s):
    if scope == c:
      count += 1
    else:
      fs = fs + scope + str(count)
      scope = c
      count =1
  fs = fs + scope + str(count)
  print(fs)
  return fs

def sol2(s):
  count = 1
  lst = []
  for i, c in enumerate(s):
    if i < len(s)-1 and s[i] == s[i+1]:
      count += 1
      continue
    else:
      lst.append((s[i], count))
      count = 1
    fs = ""
  for char,cnt in lst:
    fs = fs + char + str(cnt)
  print(fs)
  return fs


def sol3(string):
  if len(string) == 0:
    return string
  parts = []
  current_letter = string[0]
  current_count = 1
  for letter in string[1:]:
    if current_letter == letter:
      current_count += 1
    else:
      parts.append(current_letter + str(current_count))
      current_letter = letter
      current_count = 1

  parts.append(current_letter + str(current_count))
  compressed = "".join(parts)
  if len(compressed) < len(string):
    return compressed
  else:
    return string

# validation

assert sol1('aabcccccaaaz') == 'a2b1c5a3z1'
assert sol1('aabcccccaaazz') == 'a2b1c5a3z2'
assert not sol1('aseejain') == 'a2b1c5a3z2'

assert sol2('aabcccccaaaz') == 'a2b1c5a3z1'
assert sol2('aabcccccaaazz') == 'a2b1c5a3z2'
assert not sol2('aseejain') == 'a2b1c5a3z2'


