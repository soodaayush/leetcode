# https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: list[str]) -> list[str]:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]