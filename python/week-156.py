# https://leetcode.com/problems/find-center-of-star-graph/

# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1
# edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi]
# indicates that there is an edge between the nodes ui and vi. Return the
# center of the given star graph.

# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

soln = Solution()

edges = [[1,2],[2,3],[4,2]]

print(soln.findCenter(edges))