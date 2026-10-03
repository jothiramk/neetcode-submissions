class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)
        # print(target)
        i = target - 1
        dest = target -1
        while i >= 0:            
            curr_jump =  i+nums[i]
            if curr_jump>= dest:
                if i == 0:
                    return True
                else:
                    dest = i
            i-=1
            
        return False
            