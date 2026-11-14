# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

# The k-beauty of an integer num is defined as the number of substrings of num
# when it is read as a string that meet the following conditions:

# - It has a length of k.
# - It is a divisor of num.

# Given integers num and k, return the k-beauty of num.

# Note:

# - Leading zeros are allowed.
# - 0 is not a divisor of any value.

# A substring is a contiguous sequence of characters in a string.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        left = 0
        count = 0
        str_num = str(num)

        for right in range(k - 1, len(str_num)):
            substring = str_num[left:right + 1]
            substring_int = int(substring)

            if substring_int != 0 and num % substring_int == 0:
                count += 1

            left += 1

        return count


soln = Solution()

num = 2
k = 1

print(soln.divisorSubstrings(num, k))