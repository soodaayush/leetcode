# https://leetcode.com/problems/destination-city/

# You are given the array paths, where paths[i] = [cityAi, cityBi] means
# there exists a direct path going from cityAi to cityBi. Return the
# destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = defaultdict(int)

        for i in paths:
            cities[i[0]] -= 1
            cities[i[1]] += 1

        key = [k for k, v in cities.items() if v == 1]

        return key[0]

soln = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

print(soln.destCity(paths))