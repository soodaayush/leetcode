# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
# adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)




s = "aaaaaaaa"

soln = Solution()
print(soln.removeDuplicates(s))