# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array
# of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums: list[int]):
    sequence = list(range(1, len(nums) + 1))

    numSet = set(nums)

    arr = []

    for i in sequence:
        if i not in numSet:
            arr.append(i)

    return arr
