class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        goal = size - 1
        
        for i in range(size-2,-1,-1):
            # print(f'goal is {goal} and i is {i} and nums[i] is {nums[i]}')
            if i+nums[i] >= goal:
                goal = i

        return goal == 0

            
