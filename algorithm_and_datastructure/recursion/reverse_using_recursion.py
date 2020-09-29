"""
reverse string using recursion
"""

def rev(s):
    print(s)
    if len(s) == 0:
        return s
    return rev(s[1:]) + s[0]

# rev(s[1:]) + s[0]
print(rev("prem"))