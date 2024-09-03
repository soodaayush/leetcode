# https://leetcode.com/problems/single-number-ii/

# Given an integer array nums where every element appears three times except for one,
# which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra
# space.

def singleNumber(nums: list[int]):
    for i in nums:
        if nums.count(i) == 1:
            return i
