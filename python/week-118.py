# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will
# receive a discount equivalent to prices[j] where j is the minimum index such that j > i and
# prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith
# item of the shop, considering the special discount.

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        output = []

        for i, el in enumerate(prices):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    output.append(prices[i] - prices[j])
                    break

                if j == (len(prices) - 1):
                    output.append(prices[i])
                    break

        output.append(prices[-1])

        return output

soln = Solution()

prices = [1,2,3,4,5]

print(soln.finalPrices(prices))
