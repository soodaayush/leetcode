# https://leetcode.com/problems/longest-fibonacci-subarray/

# You are given an array of positive integers nums.

# A Fibonacci array is a contiguous sequence whose third and subsequent terms each equal the sum of the two preceding terms.

# Return the length of the longest Fibonacci subarray in nums.

# Note: Subarrays of length 1 or 2 are always Fibonacci.

def longestSubarray(nums: list[int]) -> int:
    length = 0
    max_length = 0

    if len(nums) == 1 or len(nums) == 2:
        return len(nums)
    else:
        length = 2

        for i in range(0, len(nums)):
            if i > 1:
                if nums[i] == (nums[i - 1] + nums[i - 2]):
                    length += 1
                else:
                    max_length = max(max_length, length)
                    length = 2

    max_length = max(max_length, length)

    return max_length