# https://leetcode.com/problems/power-of-four/

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

def isPowerOfFour(n: int) -> bool:
    if n == 1 or n == 4:
        return True

    base = 4

    while base <= n:
        base = base * 4

        if base == n:
            return True

    return False
