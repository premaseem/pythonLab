
# What is Cache?
A cache is like short-term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items. Caches can exist at all levels in architecture, but are often found at the level nearest to the front end, where they are implemented to return data quickly without taxing downstream levels.
They are used in almost every computing layer: hardware, operating systems, web browsers, web applications, and more.

## Cache invalidation 
If the data is modified in the database, it should be invalidated in the cache; if not, this can cause inconsistent application behavior.

    Write-through cache: Under this scheme, data is written into the cache and the corresponding database simultaneously.
    Write-around cache: This technique is similar to write-through cache, but data is written directly to permanent storage, bypassing the cache.
    Write-back cache: Under this scheme, data is written to cache alone, and completion is immediately confirmed to the client.

## Cache eviction policies
    Following are some of the most common cache eviction policies:
    First In First Out (FIFO): The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.
    Least Recently Used (LRU): Discards the least recently used items first.
    Least Frequently Used (LFU): Counts how often an item is needed. Those that are used least often are discarded first.
    Time To Live  (TTL): Data is remains in the cache for specific time like 300 sec and deleted after that. It can be renewed upon usage if needed. 
    Random Replacement (RR): Randomly selects a candidate item and discards it to make space when necessary.

