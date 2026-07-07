# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

# Given a circular array nums, find the maximum absolute difference between adjacent elements.

# Note: In a circular array, the first and last elements are adjacent.

class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max_diff = abs(nums[0] - nums[-1])
        arr_len = len(nums)

        for i in range(arr_len - 1):
            max_diff = max(max_diff, abs(nums[i] - nums[i + 1]))

        return max_diff

soln = Solution()
arr = [1, 2, 4]

print(soln.maxAdjacentDistance(arr))