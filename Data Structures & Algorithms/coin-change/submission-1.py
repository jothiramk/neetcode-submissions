class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp is a dict of amount to number of coins required to reach that amount
        dp = [math.inf] * (amount+1)
        dp[0]=0
        for amt in range(1,amount+1):
            for coin in coins:
                if (amt - coin ) >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
                
        
        return dp[amount] if dp[amount] != math.inf else -1


        