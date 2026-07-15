# https://leetcode.com/problems/faulty-keyboard/

# Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have
# written. Typing other characters works as expected.

# You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

# Return the final string that will be present on your laptop screen.

class Solution:
    def finalString(self, s: str) -> str:
        last_index = len(s)
        s = list(s)

        for i, el in enumerate(s):
            if el == "i":
                s = list(s[0:(i + 1)])[::-1] + list(s[(i+1):last_index])

        s = [char for char in s if char != "i"]

        return "".join(s)

soln = Solution()

s = "qskyviiiii"
print(soln.finalString(s))