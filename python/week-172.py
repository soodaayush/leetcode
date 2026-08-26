# https://leetcode.com/problems/valid-triangle-number/

# Given an integer array nums, return the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a triangle.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()

        ans = 0

        for right in range(len(nums) - 1, 1, -1):
            left = 0
            middle = right - 1

            while left < middle:
                if nums[left] + nums[middle] > nums[right]:
                    ans += middle - left
                    middle -= 1
                else:
                    left += 1

        return ans

soln = Solution()

nums = [2,2,3,4]

print(soln.triangleNumber(nums))