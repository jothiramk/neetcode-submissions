class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        result = 0
        nums.sort()
        count = 0
        print(nums)
        for j in range(1, len(nums)):
            if nums[j]==nums[j-1]:
                continue
            if nums[j]-nums[j-1]==1:              
                count +=1
                result=max(result,count)
                
            else:
                count = 0
            # i = j
                
        return result+1
        