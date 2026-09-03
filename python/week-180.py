# https://leetcode.com/problems/max-number-of-k-sum-pairs/

# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k
# and remove them from the array.

# Return the maximum number of operations you can perform on the array.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        operations = 0

        while left <= right:
            if nums[left] + nums[right] < k and left != right:
                left += 1
            elif nums[left] + nums[right] > k and left != right:
                right -= 1
            elif nums[left] + nums[right] == k and left != right:
                operations += 1
                left += 1
                right -= 1
            else:
                return operations

        return operations

soln = Solution()

nums  = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
k = 2

print(soln.maxOperations(nums, k))