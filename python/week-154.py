# https://leetcode.com/problems/max-area-of-island/

# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return 0
            if grid[r][c] != 1 or (r, c) in seen:
                return 0

            seen.add((r, c))
            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in seen:
                    max_area = max(max_area, dfs(i, j))

        return max_area

soln = Solution()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(soln.maxAreaOfIsland(grid))
