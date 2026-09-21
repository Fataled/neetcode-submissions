class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        for i, n in enumerate(prices):
           for x in range(len(prices) - 1, -1, -1): 
            if i > x:
                continue
            else:
                profit = (prices[x] - n)
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit
