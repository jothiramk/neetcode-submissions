class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return max(nums)

        # rob from house 0 to size-2
        dp= [0]*(size-1)
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2, size -1):
            dp[i]= max(nums[i]+dp[i-2],dp[i-1])
        first_iter = dp[-1]
        # print(f'first_iter {dp} and {first_iter} ')

        # rob from house 1 to size-1
        dp1= [0]*size
        dp1[1] = nums[1]
        dp1[2] = max(nums[2],nums[1])
        for i in range(3, size ):
            dp1[i]= max(nums[i]+dp1[i-2],dp1[i-1])
        second_iter = dp1[-1]
        # print(f'second_iter {dp1} and {second_iter} ')
        

        #return the max of both computations
        return max(first_iter,second_iter)