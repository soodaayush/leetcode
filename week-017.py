from math import floor

def convertnumbertobase7(num):
    if num == 0:
        return "0"

    base7 = []
    quotient = abs(num)

    while quotient > 0:
        remainder = floor(quotient % 7)

        base7.append(remainder)
        quotient = quotient // 7

    base7.reverse()
    base7 = ''.join(str(x) for x in base7)

    return base7 if num > 0 else "-" + base7


print(convertnumbertobase7(4))
