# https://leetcode.com/problems/number-of-provinces/

# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# ith city and the jth city are directly connected, and isConnected[i][j] = 0
# otherwise.

# Return the total number of provinces.

# Time Complexity: O(N^2)
# Space Complexity: O(N)

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        seen = set()
        rows = len(isConnected)
        provinces = 0

        def dfs(city):
            seen.add(city) # Add new city into set

            for i, el in enumerate(isConnected[city]):
                if el and i not in seen: # Check if isConnected[i,j] == 1 and
                    # that the index has not been seen before
                    dfs(i)

        for i in range(rows):
            if i not in seen: # Loop over every subarray and check if their
                # index has been seen
                dfs(i)
                provinces += 1

        return provinces


soln = Solution()

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

print(soln.findCircleNum(isConnected))