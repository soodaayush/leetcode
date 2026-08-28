# https://leetcode.com/problems/sum-of-square-numbers/

# Given a non-negative integer c, decide whether there're two integers a and b
# such that a^2 + b^2 = c.

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.floor(math.sqrt(c))

        while left <= right:
            statement = left * left + right * right

            if statement < c:
                left += 1
            elif statement > c:
                right -= 1
            else:
                return True

        return False

soln = Solution()

c = 3

print(soln.judgeSquareSum(c))