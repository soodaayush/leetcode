# https://leetcode.com/problems/sort-array-by-parity/

# Given an integer array nums, move all the even integers at the beginning of
# the array followed by all the odd integers.

# Return any array that satisfies this condition.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 != 0:
                right -= 1

        return nums

soln = Solution()

nums = [3,1,2,4]

print(soln.sortArrayByParity(nums))