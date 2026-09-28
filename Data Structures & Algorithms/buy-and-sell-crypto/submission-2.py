class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(l+1, len(prices)):
            if prices[r]-prices[l]<0:
                l = r
            else:
                profit = max(profit, prices[r]-prices[l])
        
        return profit
