from math import floor

class Solution:
    def convertToBase7(self, num: int) -> str:  
        base7 = []

        if num == 0:
            return "0"

        if num < 7 and num > 0:
            return str(num)  

        if num < 0 and num > -7:
            return str(num)      

        if num > 0:
            while round(num) > 0:
                base7.append(floor(num % 7))
                num = num / 7

            base7.reverse()
            base7 = ''.join(str(x) for x in base7)

            if base7[0] == "0":
                base7 = base7[1:]
        else:
            num = abs(num)

            while round(num) > 0:
                base7.append(floor(num % 7))
                num = num / 7

            base7.reverse()
            base7 = ''.join(str(x) for x in base7)

            if base7[0] == "0":
                base7 = base7[1:]

            base7 = "-" + base7

        return base7