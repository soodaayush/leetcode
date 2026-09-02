# https://leetcode.com/problems/bag-of-tokens/

# You start with an initial power of power, an initial score of 0, and a bag of
# tokens given as an integer array tokens, where each tokens[i] denotes the
# value of token_i.

# Your goal is to maximize the total score by strategically playing these
# tokens. In one move, you can play an unplayed token in one of the two ways
# (but not both for the same token):

# - Face-up: If your current power is at least tokens[i], you may play token_i,
# losing tokens[i] power and gaining 1 score.
# - Face-down: If your current score is at least 1, you may play token_i,
# gaining tokens[i] power and losing 1 score.

# Return the maximum possible score you can achieve after playing any number
# of tokens.

# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0

        while left <= right:
            if tokens[left] > power and score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
            else:
                return 0

        return score

soln = Solution()

tokens = [48,87,26]
power = 81

print(soln.bagOfTokensScore(tokens, power))