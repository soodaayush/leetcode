# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

import sys
sys.set_int_max_str_digits(0)


def trailingZeroes(n: int) -> int:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    factorial = str(factorial)

    zeros = len(factorial) - len(factorial.rstrip("0"))

    return int(zeros)


