# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.

# - For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> (
            bool):
        graph = defaultdict(set)
        possible = True

        seen = set()
        current_path = set()

        for u, v in prerequisites:
            graph[v].add(u)

        def dfs(node):
            nonlocal possible
            seen.add(node)
            current_path.add(node)

            for neighbor in graph[node]:
                if neighbor in current_path:
                    possible = False

                if neighbor not in seen:
                    dfs(neighbor)

            current_path.remove(node)

        for i in range(0, numCourses):
            if i not in seen:
                dfs(i)

        return possible


soln = Solution()

numCourses = 2
prerequisites = [[1,0],[0,1]]

print(soln.canFinish(numCourses, prerequisites))
