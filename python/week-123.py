# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums = Counter(nums).most_common(k)
        new_nums = []

        for i in nums:
            new_nums.append(i[0])

        return new_nums

soln = Solution()

nums = [1,2,2,3,3,3]
k = 2

print(soln.topKFrequent(nums, k))