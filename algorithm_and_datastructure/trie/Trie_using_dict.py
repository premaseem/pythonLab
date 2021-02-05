"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

class Trie:
    def __init__(self):
        self.root = {}
        self._end = "_end"


    def add(self,word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[self._end] = self._end

    def word_exist(self,word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.get(letter)
            if not current_dict:
                return False
        return current_dict.get(self._end) is not None



    def count_words(self):
        d = self.root
        lst = []
        cnt = 0
        if len(d) > 1: 
            lst.extend(d.keys())
        if d.get(self._end):
            cnt += 1


    def startsWith(self,c):
        d = self.root.get(c)
        if not d:
            return None
        d


t = Trie()
t.add("cat")
t.add("catter")
t.add("catter pillar")
t.add("dog")
print(t.root)
print("word exists", t.word_exist("cat"))
# t.startsWith("c")