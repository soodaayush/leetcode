# https://leetcode.com/problems/find-if-path-exists-in-graph/

# There is a bi-directional graph with n vertices, where each vertex is
# labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
# as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
# bi-directional edge between vertex ui and vertex vi. Every vertex pair
# is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex
# source to vertex destination.

# Given edges and the integers n, source, and destination, return true if
# there is a valid path from source to destination, or false otherwise.

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        validPath = False

        seen = set()
        seen.add(source)

        for u, v in edges:
            # Since this is an undirected list, establish connections in
            # both directions
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            nonlocal validPath

            for nei_node in graph[node]:
                if nei_node not in seen:
                    # Add vertex to seen and perform recursion
                    seen.add(nei_node)
                    dfs(nei_node)

                # If target is found, mark valid path as True
                if nei_node == destination:
                    validPath = True
                    return

        dfs(source)

        return validPath

soln = Solution()

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 0

print(soln.validPath(n, edges, source, destination))