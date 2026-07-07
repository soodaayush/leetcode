# https://leetcode.com/problems/sort-the-people/

# You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        people = {}
        output = []

        for i in range(0, len(names)):
            people[heights[i]] = names[i]

        sorted_people = dict(sorted(people.items()))

        for i in list(sorted_people.values())[::-1]:
           output.append(i)

        return output



soln = Solution()

names = ["Alice","Bob","Bob"]
heights = [155,185,150]

print(soln.sortPeople(names, heights))