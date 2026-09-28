class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        for i in range(n+1):
            sum+=i
            print (sum)
        
        

        for num in nums:
            sum-=num
        
        return sum