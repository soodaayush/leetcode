# https://leetcode.com/problems/find-the-degree-of-each-vertex/

# You are given a 2D integer array matrix of size n x n representing the
# adjacency matrix of an undirected graph with n vertices labeled from 0 to
# n - 1.

# - matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
# - matrix[i][j] = 0 indicates that there is no edge between vertices i and j.

# The degree of a vertex is the number of edges connected to it.

# Return an integer array ans of size n where ans[i] represents the degree of
# vertex i.

# Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        counts = []

        for i in matrix:
            counts.append(sum(i))

        return counts


soln = Solution()

matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

print(soln.findDegrees(matrix))