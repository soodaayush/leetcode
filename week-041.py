# https://leetcode.com/problems/find-peak-element/

# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
# return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be
# strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

def findPeakElement(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums.index(nums[0])

    for index, item in enumerate(nums):
        try:
            nums[index + 1]
        except IndexError:
            if item > nums[index - 1]:
                return index

        try:
            nums[index - 1]
        except IndexError:
            if item > nums[index + 1]:
                return index

        if item > nums[index - 1] and item > nums[index + 1]:
            return index
