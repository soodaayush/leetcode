# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

def appendChracters(s, t):
    s_index, t_index = 0, 0
    s_length, t_length = len(s), len(t)

    while s_index < s_length and t_index < t_length:
        if s[s_index] == t[t_index]:
            t_index += 1

        s_index += 1

    return t_length - t_index
