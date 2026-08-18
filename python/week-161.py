# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e.,
# (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# - All the visited cells of the path are 0.
# - All the adjacent cells of the path are 8-directionally connected (i.e.,
# they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        last_index = (rows - 1, cols - 1)
        seen = {(0, 0)}
        queue = deque([(0, 0)])
        directions = [(1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0,1), (0,-1)]
        shortest_distance = 1
        found = False

        if grid[0][0] == 1:
            return -1

        if (0, 0) == last_index:
            return 1

        while queue:
            shortest_distance += 1

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for i in directions:
                    new_x, new_y = i

                    dr = row + new_x
                    dc = col + new_y

                    in_bounds = (0 <= dr <= rows - 1) and (0 <= dc <= cols - 1)
                    not_seen = (dr, dc) not in seen

                    if in_bounds and not_seen and grid[dr][dc] == 0:
                        if (dr, dc) == last_index:
                            return shortest_distance

                        seen.add((dr, dc))
                        queue.append((dr, dc))

        return -1 if not found else shortest_distance

soln = Solution()

grid = [[0,0,1,0],[1,0,1,0],[1,1,0,1],[0,0,0,0]]

print(soln.shortestPathBinaryMatrix(grid))