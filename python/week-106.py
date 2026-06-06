# https://leetcode.com/problems/backspace-string-compare/

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a
# backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for i in s:
            if i == "#" and s_list:
                s_list.pop()
            elif i != "#":
                s_list.append(i)

        for j in t:
            if j == "#" and t_list:
                t_list.pop()
            elif j != "#":
                t_list.append(j)

        return s_list == t_list


s = "ab#c"
t = "ad#c"

soln = Solution()
print(soln.backspaceCompare(s, t))