def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower()
    wordCount = {}

    symbols = "!?',;."

    for i in symbols:
        paragraph = paragraph.replace(i, " ")
    paragraph = paragraph.split()

    for i in paragraph:
        if i not in wordCount:
            wordCount[i] = 0
        if i in wordCount:
            wordCount[i] += 1

    for i in banned:
        if i in wordCount:
            del wordCount[i]

    return max(wordCount, key=wordCount.get)


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
