
def addDigits(num: int):
    while num >= 10:
       num = sum(int(i) for i in str(num))
    return num


print(addDigits(84))