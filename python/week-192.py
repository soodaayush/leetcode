# https://leetcode.com/problems/maximize-greatness-of-an-array/

# You are given a 0-indexed integer array nums. You are allowed to permute nums
# into a new array perm of your choosing.

# We define the greatness of nums be the number of indices 0 <= i < nums.length
# for which perm[i] > nums[i].

# Return the maximum possible greatness you can achieve after permuting nums.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()

        ans = 0

        for num in nums:
            if nums[ans] < num:
                ans += 1

        return ans


soln = Solution()

nums = [1, 2, 3, 4]

print(soln.maximizeGreatness(nums))