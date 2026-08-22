# https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i]
# = [ai, bi] indicates that you must take course bi first if you want to take
# course ai.

# - For example, the pair [0, 1], indicates that to take course 0 you have to
#   first take course 1.

# Return the ordering of courses you should take to finish all courses. If there
# are many valid answers, return any of them. If it is impossible to finish all
# courses, return an empty array.

# Time Complexity: O(V + E) V = numCourses, E = prereq pairs
# Space Complexity: O(V + E)

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        remaining_prereqs = [0] * numCourses
        courses = []
        q = deque()

        for u, v in prerequisites:
            graph[v].append(u)
            remaining_prereqs[u] += 1

        for i, el in enumerate(remaining_prereqs):
            if el == 0:
                q.append((el, i))

        while q:
            course = q.popleft()
            courses.append(course[1])

            for i in graph[course[1]]:
                remaining_prereqs[i] -= 1

                if remaining_prereqs[i] == 0:
                    q.append((remaining_prereqs[i], i))

        return courses if len(courses) == numCourses else []

soln = Solution()

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(soln.findOrder(numCourses, prerequisites))
