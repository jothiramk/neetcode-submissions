class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        window = 0
        min_size = len(nums)
        is_target = False
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                is_target = True
                window = r - l + 1
                min_size = min(min_size, window)
                # print(f'min_size {min_size} and sum is {sum}')
                sum = sum - nums[l]
                l = l + 1
                
        # return min_size
        return (0 if not is_target else min_size)
        