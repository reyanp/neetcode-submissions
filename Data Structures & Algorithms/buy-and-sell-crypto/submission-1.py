class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        low = 10000000
        for i in range(len(prices)):
            low = min(low, prices[i])
            high = prices[i]
            maxProfit = max(maxProfit, high - low)
        
        return maxProfit

