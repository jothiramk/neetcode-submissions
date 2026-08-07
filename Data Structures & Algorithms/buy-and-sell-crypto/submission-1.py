class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_price = 0
        i = 0
        for j in range(i+1, len(prices)):
            profit = prices[j] - min(prices[j-1],buy_price)
            if profit > 0 :
                max_price = max(max_price, profit)
            buy_price = min (buy_price, prices[j])
        return max_price