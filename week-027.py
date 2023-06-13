def singleNumber(nums: list[int]):
    for i in nums:
        if nums.count(i) == 1:
            return i


print(singleNumber([2, 2, 3, 2]))
