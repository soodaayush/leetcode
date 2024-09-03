# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    uniqueLetters = ""
    a = 0

    for c in s:
        if c not in uniqueLetters:
            uniqueLetters += c
        else:
            uniqueLetters = uniqueLetters[uniqueLetters.index(c) + 1:] + c
        a = max(a, len(uniqueLetters))
    return a
