# https://leetcode.com/problems/search-a-2d-matrix/

# You are given an m x n integer matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in matrix:
        for j in i:
            if j == target:
                return True

    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
