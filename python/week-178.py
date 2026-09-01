# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Time Complexity: O(n^2)
# Space Complexity O(log n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        nums_len = len(nums)
        triplets = []

        for fixed in range(0, nums_len):
            # If fixed is positive (since all values after it are also all
            # positive) or it is a  duplicate, skip the iteration of the loop
            if nums[fixed] > 0 or (fixed != 0 and nums[fixed] == nums[fixed -
                                                                     1]):
                continue

            # Create left and right pointers
            left = fixed + 1
            right = nums_len - 1

            while left < right:
                current_sum = nums[fixed] + nums[left] + nums[right]

                # Move pointers in their corresponding directions if sum != 0
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # If triplet found, append it to the list
                    triplets.append([nums[fixed], nums[left], nums[right]])

                    # While there are duplicates, keep moving left
                    while left + 1 < nums_len and nums[left] == nums[left + 1]:
                        left += 1

                    # While there are duplicates, keep moving right
                    while right - 1 >= 0 and nums[right] == nums[right - 1]:
                        right -= 1

                    # Because we would be on the last duplicate number on
                    # left and/or left, we move both pointers to ensure we
                    # are on a new number
                    left += 1
                    right -= 1

        return triplets

soln = Solution()

nums = [0,0,0]

print(soln.threeSum(nums))