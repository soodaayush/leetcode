# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Given an integer array nums of length n where all the integers of nums are in the range
# [1, n] and each integer appears once or twice, return an array of all the integers that
# appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

import collections


def findDuplicates(nums: list[int]):
    return [key for key, value in collections.Counter(nums).items() if value == 2]
