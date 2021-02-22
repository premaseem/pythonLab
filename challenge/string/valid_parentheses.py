"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Input: s = "{[]}"
Output: true

Input: s = "([)]"
Output: false



"""

def sol( s: str) -> bool:
    m = { }
    m["}"]="{"
    m["]"]="["
    m[")"]="("
    stack = []
    for c in s:
        if c in m.values():
            stack.append(c)

        if c in m:
            try:
                if m[c] != stack.pop():
                    return False
            except:
                return False
    return not stack

def sol2(s: str) -> bool:
    while "()" in s or "{}" in s or '[]' in s:
        s = s.replace("()", "").replace('{}', "").replace('[]', "")
    return s == ''

def sol3( s: str) -> bool:
    left = ['(', '{', '[']
    right = [')', '}', ']']
    stack = []

    for c in s:
        if c in left:
            stack.append(c)
        elif c in right:
            if not stack:
                return False
            if right.index(c) != left.index(stack.pop()):
                return False

    return not stack

