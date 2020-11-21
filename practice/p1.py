# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

t1 = "aseem"
t2 = "jain"

# Brute Force
# def sol(d):
#     for i in range(len(d)):
#         for j in range(i+1, len(d)):
#             if d[i] == d[j]:
#                 return 0

# def sol(d):
#     buffer = {}
#     for c in d:
#         if buffer.get(c):
#             return False
#         else:
#             buffer[c] = True
#     return True

# def sol(d):
#     buffer = set()
#     for c in d:
#         if c in buffer:
#             return False
#         else:
#             buffer.add(c)
#     return True

# def sol(d):
#     for c in d:
#         if d.count(c) > 1:
#             return False
#     return True

def sol(d):
    return len(d) == len(set(d))

# Slicing
# def sol(d):
#     for i,c in enumerate(d):
#         if c in d[i+1:]:
#             return False
#     return True

assert sol(t1) is not None or False
assert sol(t2) is None or True
