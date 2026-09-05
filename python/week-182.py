# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

# Given two integer arrays arr1 and arr2, and the integer d, return the distance
# value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that
# there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

# Time Complexity: O(M x N)
# Space Complexity: O(1)

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int],d: int) -> int:
        arr1.sort()
        arr2.sort()
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        count = 0

        for fixed in range(0, arr1_len):
            left = 0
            right = arr2_len - 1
            valid = True

            while left <= right:
                sum = abs(arr1[fixed] - arr2[left])

                if sum <= d:
                    valid = False
                    break

                left += 1

            if valid:
                count += 1

        return count

soln = Solution()

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

print(soln.findTheDistanceValue(arr1, arr2, d))