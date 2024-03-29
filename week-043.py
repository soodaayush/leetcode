# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the
# majority element always exists in the array.

def majorityElement(nums: list[int]) -> int:
    numbersAmount = {}

    for i in nums:
        if i in numbersAmount.keys():
            continue

        numbersAmount[i] = nums.count(i)

    maxNum = max(numbersAmount, key=numbersAmount.get)

    return maxNum
