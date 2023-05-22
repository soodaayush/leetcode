def reverseWords(s: str):
    newArr = []

    s = s.split(" ")

    for i in s:
        newArr.append(i[::-1])

    newArr = ' '.join(newArr)

    return newArr


print(reverseWords("God Ding"))
