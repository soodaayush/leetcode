import string


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))

    paragraph = paragraph.translate(translator).lower().split(" ")

    wordObj = {}

    for i in paragraph:
        if i != " ":
            wordObj[i] = paragraph.count(i)

    for i in banned:
        if i in wordObj:
            del wordObj[i]

    return max(wordObj, key=wordObj.get)


print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
