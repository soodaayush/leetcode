# https://leetcode.com/problems/string-compression/

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the
# array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter
# and should be ignored.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def compress(self, chars: list[str]) -> int:
        left = 0
        right = 0
        counter = 0
        write = 0

        while left <= len(chars) - 1:
            while right <= len(chars) - 1 and chars[right] == chars[left]:
                counter += 1
                right += 1

            str_counter = str(counter)

            if counter == 1:
                chars[write] = chars[left]
                write += 1
            elif 1 < counter < 10:
                chars[write] = chars[left]
                write += 1
                chars[write] = str_counter
                write += 1
            elif counter >= 10:
                j = 0
                chars[write] = chars[left]
                write += 1

                while j <= len(str_counter) - 1:
                    chars[write] = str_counter[j]
                    j += 1
                    write += 1

            left = right
            counter = 0

        return write

soln = Solution()

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(soln.compress(chars))