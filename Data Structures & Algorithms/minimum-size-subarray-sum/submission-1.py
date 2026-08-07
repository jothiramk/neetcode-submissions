class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        window = 0
        min_size = float('inf')
        
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                is_target = True
                window = r - l + 1
                min_size = min(min_size, window)
                sum = sum - nums[l]
                l = l + 1
                
        # return min_size
        return (0 if min_size == float('inf') else min_size)
        