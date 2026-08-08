# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers nums and an integer k, return the total number
# of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        memory = defaultdict(int)
        memory[0] = 1  # Empty prefix, handles subarrays starting at index 0

        total = 0
        ans = 0

        for i in nums:
            total += i

            # If total - k was seen before, everything since then sums to k
            # Ex: if prev running total was 5 and new was 12, the sum of
            # everything in between is 7. If the total - target value
            # has been recorded in our memory before, that would mean
            # that there was a subarray that summed to k
            if total - k in memory:
                ans += memory[total - k]

            memory[total] += 1

        return ans


soln = Solution()

nums = [1, 1, 1]
k = 2

print(soln.subarraySum(nums, k))
