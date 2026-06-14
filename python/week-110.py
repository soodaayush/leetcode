# https://leetcode.com/problems/squares-of-a-sorted-array/

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result



nums = [-4,-1,0,3,10]

soln = Solution()
print(soln.sortedSquares(nums))