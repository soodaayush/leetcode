# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three
# integers at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        len_nums = len(nums)
        prev = float("-inf")

        for fixed in range(0, len_nums):
            left = fixed + 1
            right = len_nums - 1

            while left < right:
                current = nums[fixed] + nums[left] + nums[right]

                if current == target:
                    return target
                elif current < target:
                    left += 1
                else:
                    right -= 1

                if abs(target - current) < abs(target - prev):
                    prev = current

        return prev


soln = Solution()

nums = [0,3,97,102,200]
target = 300

print(soln.threeSumClosest(nums, target))