class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        n = len(prices)
        for r in range(1,n):
            if prices[l] > prices[r]:
                l = r
                continue
            profit = max(profit,prices[r]- prices[l])

        return profit