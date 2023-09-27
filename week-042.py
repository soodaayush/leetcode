# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    medianArray = nums1 + nums2
    medianArray = sorted(medianArray)

    if len(medianArray) % 2 == 1:
        return float(medianArray[len(medianArray) // 2])
    else:
        first = medianArray[len(medianArray) // 2 - 1]
        second = medianArray[len(medianArray) // 2]
        return (float(first) + float(second)) / 2
