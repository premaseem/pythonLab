# This page has definition of several concepts like hashing, heap, BST, binary search etc
# @Author:  Aseem Jain
# @Github: https://github.com/premaseem


## Hashing
Hashing is a process used to store an object according to a unique key. This means that hashing always creates a key-value pair.
Hence, the search operation can be performed in O(1).
The concept of hashing has given birth to several new data structures, but the most prominent one is the hash table.

## Hash Table
The performance of a hash table depends on three fundamental factors:

1. Hash function
2. Size of the hash table
3. Collision handling method

Ideally, list is a hash map with indexes as key, but if we use emp id as index, it would be run out the list size, and might need o(n) time operation to increase when list is resized. 
In order to limit the range of the keys to the boundaries of the list, we need a function that converts a large key into a smaller key. This is the job of the hash function.

### Hash function
A hash function simply takes an item’s key and returns the corresponding index in the list for that item.

### Strategies to Handle Collisions
1. Linear Probing: add a constant number of clashed index, until you find empty space.
2. Chaining: Save item as linked list in the same bucked ( index number)
3. Resizing the list: To avoid collision, set the threshold at 0.6, which means that when 60% of the table is filled, the resize operation needs to take place to double the size.