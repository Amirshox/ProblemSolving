class Solution:
    def solve(self, prices, k):
        prices.sort()
        result = 0
        for price in prices:
            if k >= price:
                k -= price
                result += 1
            else:
                break
        return result
