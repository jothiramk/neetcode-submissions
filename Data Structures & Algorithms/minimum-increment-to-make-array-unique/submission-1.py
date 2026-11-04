class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #did not solve, looked for paypal
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                diff = 1 + nums[i - 1]  - nums[i]
                res += diff
                nums[i] = nums[i - 1] + 1
        return res