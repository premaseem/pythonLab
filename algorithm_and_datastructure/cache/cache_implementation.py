"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

# What is Cache?
A cache is like short-term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items. Caches can exist at all levels in architecture, but are often found at the level nearest to the front end, where they are implemented to return data quickly without taxing downstream levels.

# Following are some of the most common cache eviction policies:
    First In First Out (FIFO): The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.
    Least Recently Used (LRU): Discards the least recently used items first.
    Least Frequently Used (LFU): Counts how often an item is needed. Those that are used least often are discarded first.
    Time To Live  (TTL): Data is remains in the cache for specific time like 300 sec and deleted after that. It can be renewed upon usage if needed.
    Random Replacement (RR): Randomly selects a candidate item and discards it to make space when necessary.

"""


def sol(n):
    return n * 2


test_data = [
    (2, 4),
    (4, 8),
]

for given, expected in test_data:
    assert expected == sol(given)
    print(f"Test passed for: given {given} and expected = {expected}")
