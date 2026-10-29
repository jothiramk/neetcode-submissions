class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            second_val = target - num
            # print(f'{second_val} and {nums[i+1:]}')
            if second_val in nums[i+1:]:
                index = nums.index(second_val,i+1)
                res = [i,index]
                return res
        return res

        
        