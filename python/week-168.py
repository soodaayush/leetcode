# https://leetcode.com/problems/long-pressed-name/

# Your friend is typing his name into a keyboard. Sometimes, when typing a
# character c, the key might get long pressed, and the character will be
# typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            # If chars are the same, increment both pointers
            if name[i] == typed[j]:
                i += 1
                j += 1
            # If name char is not equal to typed char but previous type char
            # is the same as the current (meaning repeating char), increment
            # typing pointer
            elif typed[j] == typed[j - 1] and j != 0:
                j += 1
            else:
                # If all else fails, it is not a long pressed name
                return False

        # If name pointer runs out and typing pointer still has left over
        # chars, check if leftover typing chars are the same as the previous
        # typing char
        if i == len(name):
            return typed[j:] == typed[j - 1] * (len(typed) - j)
        # If typing pointer runs out and name pointer still has left over
        # chars, return False
        elif j == len(typed) and i < len(name):
            return False

        return True

soln = Solution()

name = "alex"
typed = "aaleexa"

print(soln.isLongPressedName(name, typed))