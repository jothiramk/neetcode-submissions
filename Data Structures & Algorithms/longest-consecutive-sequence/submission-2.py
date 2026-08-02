class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        res = 1
        temp_res = 1
        # 1,2,5,6,7
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] == 1:
                temp_res += 1
            else:
                temp_res = 1
            res = max(temp_res,res)
        
        return res
            
