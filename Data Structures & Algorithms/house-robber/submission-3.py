class Solution:
    def rob(self, nums: List[int]) -> int:
        #check solution 3, diff appraoch to bottom up 
        size = len(nums)
        if size<3:
            return max(nums)
        dp = [0] * (size)

        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2,size):
            if i-3 < 0:
                max_sofar = dp[i-2]
            else:
                max_sofar = max(dp[i-2],dp[i-3] )
            dp[i]= max_sofar + nums[i]
            # print(f' max_sofar is {max_sofar} and dp[i] {dp[i]}')
        
        print(dp)
        return max(dp)