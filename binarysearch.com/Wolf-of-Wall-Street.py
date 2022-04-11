class Solution:
    def solve(self, prices):
        if len(prices) < 2:
            return 0
        maxProfit = 0
        min = prices[0]
        for i in prices[1:]:
            if i - min > maxProfit:
                maxProfit = i - min
            if i < min:
                min = i
        return maxProfit
