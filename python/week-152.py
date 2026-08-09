# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are
# n vertical lines drawn such that the two endpoints of the
# ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Two pointer solution

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Compute max area using index distance and minimum line height
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            # If leftmost line is smaller than rightmost line, increment left pointer by 1
            # If rightmost line is smaller than leftmost line, decrement right pointer by 1
            if min(height[left], height[right]) == height[left]:
                left += 1
            else:
                right -= 1

        return max_area

soln = Solution()

height = [1,8,6,2,5,4,8,3,7]

print(soln.maxArea(height))