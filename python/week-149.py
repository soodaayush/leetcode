# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or
# equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float("inf")

        left = 0
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1

        if min_len == float("inf"):
            min_len = 0

        return min_len


soln = Solution()

target = 7
nums = [2, 3, 1, 2, 4, 3]

print(soln.minSubArrayLen(target, nums))