class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        sum = nums[0]

        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0
            sum+= nums[i]
            result = max(sum,result)
        return result