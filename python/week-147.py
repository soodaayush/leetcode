# https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's
# (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        seen = set()
        grid_rows = len(grid) - 1
        grid_cols = len(grid[0]) - 1

        islands = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(coordinate):
            if grid[coordinate[0]][coordinate[1]] != "1":
                return

            seen.add(coordinate)

            for x, y in directions:
                row, col = coordinate
                new_x = row + x
                new_y = col + y
                new_coordinate = (new_x, new_y)

                if (0 <= new_x <= grid_rows) and (0 <= new_y <= grid_cols) and new_coordinate not in seen and grid[new_x][new_y] == "1":
                    dfs(new_coordinate)

        for row in range(grid_rows + 1):
            for col in range(grid_cols + 1):
                if (row, col) not in seen and grid[row][col] == "1":
                    dfs((row, col))
                    islands += 1

        return islands

soln = Solution()


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(soln.numIslands(grid))