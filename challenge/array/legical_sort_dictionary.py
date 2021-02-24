"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # grab a word
        # iterate the character and find index of character and compare it must be greater then last char
        pi = -1
        for i, word in enumerate(words):
            c = word[0]
            # for c in word:
            ci = order.index(c)
            if ci < pi:
                return False
            if ci == pi:
                if not self.compare_word(words[i-1],words[i],order):
                    return False
            pi = ci

        return True

    def compare_word(self,w1,w2,order):
        for c1,c2 in zip(w1,w2):
            if order.index(c1) > order.index(c2):
                return False
            if order.index(c1) < order.index(c2):
                return True
        if len(w1) > len(w2):
            return False
        return True


def sol2(self, words: List[str], order: str) -> bool:
    return words == sorted(words,key=lambda word:[order.index(c) for c in word])

