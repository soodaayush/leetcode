# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty
# substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right
# substring.

class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = 0
        right_ones = s.count("1")
        best = 0

        for char in s[:-1]:
            if char == "0":
                left_zeros += 1
            if char == "1":
                right_ones -= 1

            best = max(best, left_zeros + right_ones)

        return best



soln = Solution()
s = "00"

print(soln.maxScore(s))