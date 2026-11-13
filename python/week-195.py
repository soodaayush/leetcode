# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

# You are given a 0-indexed string blocks of length n, where blocks[i] is either
# 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B'
# denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive
# black blocks.

# In one operation, you can recolor a white block such that it becomes a black
# block.

# Return the minimum number of operations needed such that there is at least
# one occurrence of k consecutive black blocks.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        min_white = 0

        for i in range(k):
            if blocks[i] == "W":
                min_white += 1

        current_count = min_white

        for right in range(k, len(blocks)):
            if blocks[left] == "W":
                current_count -= 1

            if blocks[right] == "W":
                current_count += 1

            left += 1

            min_white = min(min_white, current_count)

        return min_white

soln = Solution()

blocks = "WBBWWBBWBW"
k = 7

print(soln.minimumRecolors(blocks, k))