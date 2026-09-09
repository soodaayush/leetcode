# https://leetcode.com/problems/number-of-arithmetic-triplets/

# You are given a 0-indexed, strictly increasing integer array nums and a
# positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the
# following conditions are met:

# - i < j < k,
# - nums[j] - nums[i] == diff, and
# - nums[k] - nums[j] == diff.

# Return the number of unique arithmetic triplets.

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums.sort()
        nums_len = len(nums)
        count = 0

        for fixed in range(0, nums_len):
            left = fixed + 1
            right = nums_len - 1

            while left <= right:
                if (fixed < left < right and abs(nums[left] - nums[fixed]) ==
                        diff and abs(nums[right] - nums[left]) == diff):
                    count += 1
                    left += 1
                    right -= 1
                elif fixed < left < right and abs(nums[left] - nums[
                    fixed]) < diff or abs(nums[right] - nums[left]) < diff:
                    left += 1
                else:
                    right -= 1

        return count

soln = Solution()

nums = [0,1,4,6,7,10]
diff = 3

print(soln.arithmeticTriplets(nums, diff))