# https://leetcode.com/problems/duplicate-zeros/

# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return
# anything.

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        right = len(arr) - 1
        arr_len = len(arr)

        while left <= right:
            if arr[left] == 0:
                arr.insert(left + 1, 0)
                left += 2
                right += 1
                continue
            else:
                left += 1
            if arr[right] == 0:
                arr.insert(right + 1, 0)
                right -= 1
            else:
                right -= 1

        arr[:] = arr[0:arr_len]

        return arr

soln = Solution()

arr = [0,4,1,0,0,8,0,0,3]

print(soln.duplicateZeros(arr))