# https://leetcode.com/problems/add-digits/

# Given an integer num, repeatedly add all its digits until the result has only one digit, and
# return it.

def addDigits(num: int):
    while num >= 10:
        num = sum(int(i) for i in str(num))
    return num


print(addDigits(84))
