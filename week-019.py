# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Given two strings needle and haystack, return the index of the first occurrence of needle
# in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1