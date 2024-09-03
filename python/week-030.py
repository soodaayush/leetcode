# https://leetcode.com/problems/sum-multiples/

# Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that
# are divisible by 3, 5, or 7.

# Return an integer denoting the sum of all numbers in the given range satisfying the
# constraint.

def sumOfMultiples(n: int):
    divisibleNums = []

    ranges = list(range(1, n + 1))

    for i in ranges:
        if i % 3 == 0:
            divisibleNums.append(i)
        elif i % 5 == 0:
            divisibleNums.append(i)
        elif i % 7 == 0:
            divisibleNums.append(i)

    return sum(divisibleNums)