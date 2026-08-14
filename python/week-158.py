# https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:
# - 0 representing an empty cell,
# - 1 representing a fresh orange, or
# - 2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    seen.add((i, j))
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue:
            level_size = len(queue)
            fresh_before = fresh

            for _ in range(level_size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    in_bounds = (0 <= new_row <= rows - 1 and 0 <= new_col <= cols
                                 - 1)
                    not_visited = (new_row, new_col) not in seen

                    if in_bounds and not_visited:
                        is_fresh = grid[new_row][new_col] == 1

                        if is_fresh:
                            seen.add((new_row, new_col))
                            fresh -= 1
                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = 2

            if fresh_before != fresh:
                time += 1

        return time if fresh == 0 else -1


soln = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]

print(soln.orangesRotting(grid))