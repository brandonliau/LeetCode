class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min, profit = prices[0], 0

        for price in prices:
            if price < min:
                min = price
            if price - min > profit:
                profit = price - min 
        
        return profit
    