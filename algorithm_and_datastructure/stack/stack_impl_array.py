# Aseem Jain

## DEFINITION:
# Stacks follow the Last in First Out (LIFO) ordering. This means that the last element added is the element on the top and the first element added is at the bottom.

## ANALOGY
# A real-life example of Stack could be a stack of books. So, in order to get the book that’s somewhere in the middle, you will have to remove all the books placed at the top of it. Also, the last book you added to the stack of books is at the top!

## USAGE
# Reversing
# Undo functionality
# Depth First Search
# Expression Evaluation Algorithm

## FUNCTIONS

# push -> adds element on top
# pop -> pop out element on top
# top or peek -> element on top
# is_empty -> boolean
# size() -> current size of stack

# Run time complexity of all operations is Time O(1)


class StackArray:
    """ Stack implementation using array is straight forward as all
    operations are provided by array list """

    def __init__(self):
        self.arr = []

    def push(self, e):
        self.arr.append(e)

    def pop(self):
        if self.arr:
            return self.arr.pop()

    def top(self):
        if self.arr:
            return self.arr[-1]

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def display(self):
        print(self.arr)


s = StackArray()
s.push(20)
print(s.top())
print(s.pop())
print(s.size())
print(s.is_empty())
s.display()

















