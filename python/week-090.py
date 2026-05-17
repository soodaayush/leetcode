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