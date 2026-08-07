# https://leetcode.com/problems/flood-fill/

# You are given an image represented by an m x n grid of integers image,
# where image[i][j] represents the pixel value of the image. You are also
# given three integers sr, sc, and color. Your task is to perform a flood
# fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:
# 1. Begin with the starting pixel and change its color to color.
# 2. Perform the same process for each pixel that is directly adjacent
# (pixels that share a side with the original pixel, either horizontally
# or vertically) and shares the same color as the starting pixel.
# 3. Keep repeating this process by checking neighboring pixels of the
# updated pixels and modifying their color if it matches the original
# color of the starting pixel.
# 4. The process stops when there are no more adjacent pixels of the original
# color to update.

# Return the modified image after performing the flood fill.

# Time Complexity: O(M * N) M = number of rows, N = number of columns
# Space Complexity: O(M * N)

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        grid_rows = len(image) - 1
        grid_cols = len(image[0]) - 1
        targeted_node = image[sr][sc]

        visited = set()

        if targeted_node == color:
            return image

        def dfs(node, coordinate):
            nonlocal color, targeted_node

            if node == targeted_node and coordinate not in visited:
                image[coordinate[0]][coordinate[1]] = color
                visited.add(coordinate)

                if coordinate[0] - 1 >= 0:
                    dfs(image[coordinate[0] - 1][coordinate[1]], (coordinate[0] - 1, coordinate[1]))
                if coordinate[0] + 1 <= grid_rows:
                    dfs(image[coordinate[0] + 1][coordinate[1]], (coordinate[0] + 1, coordinate[1]))
                if coordinate[1] - 1 >= 0:
                    dfs(image[coordinate[0]][coordinate[1] - 1], (coordinate[0], coordinate[1] - 1))
                if coordinate[1] + 1 <= grid_cols:
                    dfs(image[coordinate[0]][coordinate[1] + 1], (coordinate[0], coordinate[1] + 1))
            else:
                return

        dfs(image[sr][sc], (sr, sc))

        return image


soln = Solution()

image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2

print(soln.floodFill(image, sr, sc, color))