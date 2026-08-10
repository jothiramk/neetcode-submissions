class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find if there is a cycle first
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #then find the head of the cycle, here it will be the rpeasting number 
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow