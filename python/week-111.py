# https://leetcode.com/problems/word-pattern/

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Specifically:
#     Each letter in pattern maps to exactly one unique word in s.
#     Each unique word in s maps to exactly one letter in pattern.
#     No two letters map to the same word, and no two words map to the same letter.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = {}
        s = s.split()

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in patterns:
                if s[i] in patterns.values():
                    return False
                patterns[pattern[i]] = s[i]
            elif s[i] != patterns[pattern[i]]:
                return False

        return True




pattern = "aaa"
s = "aa aa aa aa"

soln = Solution()
print(soln.wordPattern(pattern, s))