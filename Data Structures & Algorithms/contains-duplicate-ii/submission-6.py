class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()
        for r in range(len(nums)):
            #if the window size exceeds reset. 
            # print(f' l is {l} and r is{r} and nums[r] is {nums[r]}')
            if r - l   > k:
                window.remove(nums[l])
                l = l + 1
                # print(f'removed window is {window}')
            if nums[r] not in window:
                window.add(nums[r])
                # print(f'window is {window}')
            else:
                return True
            
        
        return False