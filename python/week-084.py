# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

def longestSubarray(nums: list[int]) -> int:
    zero_count = 0
    max_length = 0

    left = 0
    right = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(((right - left), max_length))

    if zero_count == 0:
        return len(nums) - 1
    else:
        return max_length
