# https://leetcode.com/problems/spiral-matrix/

# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(matrix: list[list[int]]) -> list[int]:
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        top = 0
        spiral = []
        indices = []

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
                indices.append([top, i])
            top += 1

            for j in range(top, bottom + 1):
                spiral.append(matrix[j][right])
                indices.append([j, right])
            right -= 1

            if top <= bottom:
                for k in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][k])
                    indices.append([bottom, k])
                bottom -= 1

                if right >= 0:
                    for l in range(bottom, top - 1, -1):
                        if [l, left] not in indices:
                            spiral.append(matrix[l][left])
                            indices.append([l, left])
                    left += 1

        return spiral
