# https://leetcode.com/problems/as-far-from-land-as-possible/

# Given an n x n grid containing only values 0 and 1, where 0 represents water
# and 1 represents land, find a water cell such that its distance to the nearest
# land cell is maximized, and return the distance. If no land or water exists in
# the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)

from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_distance = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: # Add all land to queue
                    seen.add((i, j))
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == rows * cols:
            return -1

        while queue:
            level_size = len(queue)
            max_distance += 1 # Once all previous land has been evaluated,
            # increment max_distance by 1

            for _ in range(level_size): # Loop for all available land
                # BFS

                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    in_bounds = (0 <= new_row <= rows - 1 and 0 <= new_col <= cols
                                 - 1)
                    not_visited = (new_row, new_col) not in seen

                    if (in_bounds and not_visited and grid[new_row][new_col]
                            == 0):
                        grid[new_row][new_col] = 1
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col)) # Add new land to
                        # queue to keep checking for more water

        return max_distance - 1



soln = Solution()

grid = [[1,0,1],[0,0,0],[1,0,1]]

print(soln.maxDistance(grid))