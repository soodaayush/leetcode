# https://leetcode.com/problems/set-matrix-zeroes/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        locations = []
        length = len(matrix[0])
        columns = len(matrix)

        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for index, el in enumerate(matrix[i]):
                    if el == 0:
                        locations.append([i, index])

        for i in locations:
            matrix[i[0]] = [0] * length

            for j in range(columns):
                matrix[j][i[1]] = 0

        return matrix
