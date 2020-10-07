"""
make sure you install package from setup.py

"""
# from words.generator import random_word
from folder1.mymodule import func1
from folder2.mymodule import func2

func1("first")
func2("first")

# Defined `random_words` and `random_word` but we're only importing one directly
from words.generator import random_word

# *Only* provides `random_words` when the package is imported directly
from words import *

print(f"Random word generated: {random_word()}")
print(f"Random list of words: {random_words(5)}")
