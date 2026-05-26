# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
        length = len(nums)
        output = [0] * length

        suffix = 1
        prefix = 1

        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(length - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output