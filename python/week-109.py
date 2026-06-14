# https://leetcode.com/problems/merge-strings-alternately/

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
# word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        i = 0

        while i < len(word1) and i < len(word2):
            new_word.append(word1[i])
            new_word.append(word2[i])
            i += 1

        new_word.append(word1[i:])
        new_word.append(word2[i:])

        return "".join(new_word)


word1 = "ab"
word2 = "pqrs"

soln = Solution()
print(soln.mergeAlternately(word1, word2))