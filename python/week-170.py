# https://leetcode.com/problems/reverse-only-letters

# Given a string s, reverse the string according to the following rules:

# - All the characters that are not English letters remain in the same position.
# - All the English letters (lowercase or uppercase) should be reversed.

# Return s after reversing it.

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        s = list(s)

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] not in letters:
                left += 1

            if s[right] not in letters:
                right -= 1

            if left <= right and s[left] in letters and s[right] in letters:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

soln = Solution()

s = "ab-cd"

print(soln.reverseOnlyLetters(s))