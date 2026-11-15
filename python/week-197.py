# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

# You are given a 0-indexed integer array nums, where nums[i] represents the
# score of the ith student. You are also given an integer k.

# Pick the scores of any k students from the array so that the difference
# between the highest and the lowest of the k scores is minimized.

# Return the minimum possible difference.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        minimum_difference = float("inf")

        for right in range(k - 1, len(nums)):
            minimum_difference = min(minimum_difference, nums[right] - nums[
                right - (k - 1)])

        return minimum_difference

soln = Solution()

nums = [9, 4, 1, 7]
k = 2

print(soln.minimumDifference(nums, k))