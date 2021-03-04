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
        self.data = [ chr(ord("a")+x) for x in range(10)]

    def evict(self):
        """ Based on FIFO ie First in First out """
        queue = list(self.cache.keys())
        front_element = queue[0]
        self.cache.pop(front_element)

    def load_cache(self, x):
        if len(self.cache.keys()) >= self.capacity:
            self.evict()
        self.cache[x] = [1]

    def get_data(self, x):
        if self.cache.get(x):
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

    # till 5th element, it will hit
    ("a", "hit"),
    ("f", "miss"),

    # after overcapacity, it will evict and will miss
    ("a", "miss"),

    # it will reload again and evict front element in queue
    ("a", "hit"),
    ("b", "miss")

]

# Create capacity with 5
my_cache = Cache(5)
for given, expected in test_data:
    assert expected == my_cache.get_data(given)
    print(my_cache.cache.keys())
    print(f"Test passed for: given {given} and expected = {expected}")
