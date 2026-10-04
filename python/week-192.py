class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()

        ans = 0

        for num in nums:
            if nums[ans] < num:
                ans += 1

        return ans


soln = Solution()

nums = [1, 2, 3, 4]

print(soln.maximizeGreatness(nums))