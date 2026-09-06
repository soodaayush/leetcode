# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each
# element in the result must be unique, and you may return the result in any order.

# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        answer = []

        left = 0
        right = 0

        while left < nums1_len and right < nums2_len:
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            elif not answer or nums1[left] != answer[-1]:
                answer.append(nums1[left])
                left += 1
                right += 1
            else:
                left += 1
                right += 1

        return answer

soln = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(soln.intersection(nums1, nums2))
