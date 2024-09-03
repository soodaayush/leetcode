# https://leetcode.com/problems/third-maximum-number/

# Given an integer array nums, return the third distinct maximum number in this array. If the third
# maximum does not exist, return the maximum number.

def thirdMax(nums: list[int]) -> int:
    nums = sorted(list(set(nums)))

    if len(nums) > 2:
        return nums[-3]
    else:
        return nums[-1]
