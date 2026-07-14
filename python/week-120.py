# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

# Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common
# divisor of the subarray's elements is k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

from math import gcd


class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            current_gcd = 0

            for j in range(i, len(nums)):
                current_gcd = gcd(current_gcd, nums[j])

                if current_gcd == k:
                    count += 1

        return count


soln = Solution()

nums = [9,3,1,2,6,3]
k = 3

print(soln.subarrayGCD(nums, k))