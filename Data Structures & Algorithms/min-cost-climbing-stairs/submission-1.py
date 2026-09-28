class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        # if size <=2:
        #     return min(cost)
        
        dp = [0] * (size+1)
        dp[0]= cost[0]
        dp[1]= cost[1]

        for i in range(2, size+1):
            min_step_i = min(dp[i-2],dp[i-1])
            if i == size:
                dp[i] = min_step_i    
            else:
                dp[i] = cost[i]+min_step_i
        print(dp)
        return dp[size]
