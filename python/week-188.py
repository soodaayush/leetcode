# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

# You have an array of floating point numbers averages which is initially empty.
# You are given an array nums of n integers where n is even.

# You repeat the following procedure n / 2 times:
# - Remove the smallest element, minElement, and the largest element maxElement,
# from nums.
# - Add (minElement + maxElement) / 2 to averages.

# Return the minimum element in averages.

# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1
        averages = []

        while left <= right:
            averages.append((nums[left] + nums[right]) / 2)

            left += 1
            right -= 1

        return min(averages)


soln = Solution()

nums = [7,8,3,4,15,13,4,1]

print(soln.minimumAverage(nums))