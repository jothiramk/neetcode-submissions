class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i,num in enumerate(nums):
            value = target - num
            if value in nums[i+1:]:
                print(value)
                index = nums.index(value,i+1)
                if index >=0:
                    return [i,index]
            
                