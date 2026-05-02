# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and
# every lowercase occurrence of c appears before the first uppercase occurrence of c.

# Return the number of special letters in word.

def numberOfSpecialChars(word: str) -> int:
    first_upper = {}
    last_lower = {}

    special_chars = 0

    for i, ch in enumerate(word):
        if ch.islower():
            last_lower[ch] = i
        else:
            if ch not in first_upper:
                first_upper[ch] = i

    for ch in last_lower:
        if ch.upper() in first_upper:
            if last_lower[ch] < first_upper[ch.upper()]:
                special_chars += 1

    return special_chars

