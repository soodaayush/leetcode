# https://leetcode.com/problems/01-matrix/

# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.

# The distance between two cells sharing a common edge is 1.

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        seen = set()
        queue = deque([])
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        nearest_one = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    seen.add((i, j))
                    queue.append((i, j))

        while queue:
            nearest_one += 1

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for i in directions:
                    new_row, new_col = i

                    dr = row + new_row
                    dc = col + new_col

                    in_bounds = (0 <= dr <= rows - 1 and 0 <= dc <=
                                 cols - 1)
                    not_seen = (dr, dc) not in seen

                    if in_bounds and not_seen:
                        if mat[dr][dc] == 1:
                            seen.add((dr, dc))
                            queue.append((dr, dc))
                            mat[dr][dc] = nearest_one

        return mat


soln = Solution()

mat = [[0,0,0],[0,1,0],[1,1,1]]

print(soln.updateMatrix(mat))
