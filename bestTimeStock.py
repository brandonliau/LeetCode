class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min, max, maxDiff = prices[0], -1, 0
        for price in prices:
            if (price < min):
                min = price
                max = -1
            elif (price > max):
                max = price
            if (max - min > maxDiff):
                maxDiff = max - min
        return maxDiff

class OptimalSolution:
    def maxProfit(self, prices: list[int]) -> int:
        min, profit = prices[0], 0
        for price in prices:
            if price < min:
                min = price
            if price - min > profit:
                profit = price - min 
        return profit
