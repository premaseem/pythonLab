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

class Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = { }

    def evict(self):
        """ Based on Least Frequently used ie unused items would be evicted """

        least_frequently_used = sorted(self.cache.items(),key=lambda x:x[1])[0][0]
        print("popping ", least_frequently_used)
        self.cache.pop(least_frequently_used)

    def load_cache(self, x):
        if len(self.cache) >= self.capacity:
            self.evict()
        self.cache[x] = [1]


    def get_data(self, x):
        v = self.cache.get(x)
        if v:
            v.append(1)
            return "hit"

        self.load_cache(x)
        return "miss"


test_data = [
    ("a", "miss"),
    ("a", "hit"),
    ("b", "miss"),
    ("b", "hit"),
    ("a", "hit"),
    ("c", "miss"),
    ("d", "miss"),
    ("e", "miss"),

    # # till 5th element, it will hit
    ("a", "hit"),
    ("a", "hit"),
    ("f", "miss"),
    ("g", "miss"),
    ("g", "hit"),
    ("h", "miss"),
    ("i", "miss"),
    #
    # # after overcapacity, it will evict and least used item
    ("e", "miss"),
    ("z", "miss"),
    ("f", "miss"),
    #
    # # it will reload again and evict front element in queue
    # ("c", "hit"),
    # ("d", "miss"),
    # ("z", "miss"),
    # ("z", "hit"),
    # ("b", "miss"),
    # ("b", "hit"),
    # ("d", "hit")

]

# Create capacity with 5
my_cache = Cache(5)
for given, expected in test_data:
    print("Cache ", my_cache.cache)
    print(f"Testing with given = {given} and expected = {expected}")
    assert expected == my_cache.get_data(given)

