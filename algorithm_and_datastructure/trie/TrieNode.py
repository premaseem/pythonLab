"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # Total size of the English alphabet
        self.is_end_word = False  # True if the node represents the end of word
        self.char = char  # To store the value of a particular key

    # Function to mark the currentNode as Leaf
    def mark_as_leaf(self):
        self.is_end_word = True

    # Function to unMark the currentNode as Leaf
    def unmark_as_Leaf(self):
        self.is_end_word = False
