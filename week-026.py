# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only
# number in the range that is missing from the array.

def missingNumber(nums: list[int]):
    rangeArr = list(range(0, len(nums) + 1))

    for i in rangeArr:
        if i not in nums:
            return i