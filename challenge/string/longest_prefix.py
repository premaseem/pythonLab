#  Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, s: [str]) -> str:
        if not s:
            return ""
        sw = min(s)

        for i in range(len(sw)):
            for word in s:
                if sw[:i + 1] != word[:i + 1]:
                    return sw[:i]

        return sw