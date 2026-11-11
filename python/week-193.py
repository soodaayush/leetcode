# https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and
# abs(i - j) <= k.

# Time Complexity: O(n)
# Space Complexity: O(k)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False

        left = 0
        num_set = set()

        for right in range(len(nums)):
            if nums[right] in num_set:
                return True

            # Ensure window (the set) has at most k elements
            if len(num_set) + 1 > k:
                num_set.remove(nums[left])
                left += 1

            num_set.add(nums[right])

        return False


soln = Solution()

nums = [1,2,3,1,2,3]
k = 2

print(soln.containsNearbyDuplicate(nums, k))