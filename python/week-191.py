# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

# You are given a positive integer array skill of even length n where skill[i]
# denotes the skill of the ith player. Divide the players into n / 2 teams of
# size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players
# on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no
# way to divide the players into teams such that the total skill of each team
# is equal.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        left = 0
        right = len(skill) - 1
        chemistry = 0
        team_skill = 0

        while left <= right:
            new_skill = skill[left] + skill[right]

            if new_skill != team_skill and team_skill != 0:
                return -1

            chemistry += skill[left] * skill[right]
            team_skill = new_skill

            left += 1
            right -= 1

        return chemistry

soln = Solution()

skill = [3,2,5,1,3,4]

print(soln.dividePlayers(skill))