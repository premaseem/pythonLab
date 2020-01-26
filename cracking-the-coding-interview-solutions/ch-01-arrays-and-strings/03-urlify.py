# Replace spaces in the middle of a string with "%20" assuming the end of the 
# string contains twice as many spaces as are in the middle.

# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def sol1(s):
  return str(s).replace(" ", "%20")

def sol2(s):
  s = str(s).strip()
  arr = str(s).split(" ")
  fs = ""
  for a in arr:
    fs = fs + a + "%20"
  return fs[:-3]

def sol3(s):
  s = str(s).strip()
  arr = str(s).split(" ")
  return "%20".join(arr)

def sol4(string):
  # Convert string to list to prepare to be modified
  letters = list(string)
  i = len(letters) - 1
  j = i
  while letters[i] == " ":
    i -= 1
  while j != i:
    # Replace space with %20
    if letters[i] == " ":
      letters[j-2] = "%"
      letters[j-1] = "2"
      letters[j]   = "0"
      j -= 2
    # Copy the original character
    else:
      letters[j] = letters[i]
    i -= 1
    j -= 1
  return ''.join(letters)

print(f"The result is {sol1('Mr John Smith') == 'Mr%20John%20Smith'}")
print(f"The result is {sol1('Mr John Smith') == 'Mr%20John Smith'}")

print(f"The result is {sol2('Mr John Smith') == 'Mr%20John%20Smith'}")
print(f"The result is {sol2('Mr John Smith') == 'Mr%20John Smith'}")

print(f"The result is {sol3('Mr John Smith') == 'Mr%20John%20Smith'}")
print(f"The result is {sol3('Mr John Smith') == 'Mr%20John Smith'}")

print(f"The result is {sol4('Mr John Smith    ') == 'Mr%20John%20Smith'}")
print(f"The result is {sol4('Mr John Smith') == 'Mr%20John Smith'}")