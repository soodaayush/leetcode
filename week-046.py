def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower()

    symbols = "!?',;."

    for i in symbols:
        paragraph = paragraph.replace(i, " ")
    paragraph = paragraph.split()

    print(paragraph)


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
