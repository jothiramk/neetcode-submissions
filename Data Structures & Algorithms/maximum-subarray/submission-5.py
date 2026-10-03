class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        sub_sum = 0
        for num in nums:
            sub_sum += num
            result = max(result,sub_sum)
            if sub_sum < 0:
                sub_sum = 0
        return result
