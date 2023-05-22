# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Given a string s, reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.

def reverseWords(s: str):
    newArr = []

    s = s.split(" ")

    for i in s:
        newArr.append(i[::-1])

    newArr = ' '.join(newArr)

    return newArr