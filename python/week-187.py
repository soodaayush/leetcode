# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] +
# nums[j] < target.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        nums_len = len(nums)
        count = 0

        for fixed in range(0, nums_len):
            left = fixed + 1

            while left <= nums_len - 1:
                if nums[fixed] + nums[left] < target:
                    count += 1

                left += 1

        return count

soln = Solution()

nums = [-1,1,2,3,1]
target = 2

print(soln.countPairs(nums, target))