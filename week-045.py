# https://leetcode.com/problems/number-of-segments-in-a-string/

# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

def countSegments(s: str) -> int:
    s = s.split(" ")

    s[:] = [i for i in s if i]

    return len(s)
