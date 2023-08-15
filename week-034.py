def lengthOfLongestSubstring(s: str) -> int:
    letterLength = []
    letterArr = []
    temp = ""

    for i in [*s]:
        if i in letterArr:
            temp = temp.join(letterArr)
            letterArr = []
            letterLength.append(len(temp))
            temp = ""

        letterArr.append(i)

    print(letterLength)
    return max(letterLength)




print(lengthOfLongestSubstring("abcabcbb"))
