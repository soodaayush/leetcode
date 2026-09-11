# https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

# You are given a 0-indexed integer array nums having length n, an integer
# indexDifference, and an integer valueDifference.

# Your task is to find two indices i and j, both in the range [0, n - 1], that
# satisfy the following conditions:
# - abs(i - j) >= indexDifference, and
# - abs(i - j) >= indexDifference, and

# Return an integer array answer, where answer = [i, j] if there are two such
# indices, and answer = [-1, -1] otherwise. If there are multiple choices for
# the two indices, return any of them.

# Note: i and j may be equal.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int,
                    valueDifference: int) -> List[int]:

        nums_len = len(nums)

        for fixed in range(0, nums_len):
            left = fixed

            while left <= nums_len - 1:
                if (abs(left - fixed) >= indexDifference and abs(nums[fixed] -
                                                                nums[left]) >=
                        valueDifference):
                    return [fixed, left]

                left += 1

        return [-1, -1]

soln = Solution()

nums = [5,0,3]
indexDifference = 1
valueDifference = 4

print(soln.findIndices(nums, indexDifference, valueDifference))