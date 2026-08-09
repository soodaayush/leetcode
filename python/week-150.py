# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        grouped = []

        for i in strs:
            anagrams["".join(sorted(i))].append(i)

        for i in anagrams.values():
            grouped.append(i)

        return grouped

soln = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(soln.groupAnagrams(strs))
