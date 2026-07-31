class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        j = len(nums) - 1
        for i in range(len(nums)):
            second_num = target-nums[i]
            for j in range(i+1,len(nums)) :
                if second_num == nums[j] :
                    result.extend([i,j])
                    break
        return result