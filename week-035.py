def findTheDifference(s: str, t: str) -> str:
    for i in t:
        if s.count(i) != t.count(i):
            return i


print(findTheDifference("abcd", "abcde"))