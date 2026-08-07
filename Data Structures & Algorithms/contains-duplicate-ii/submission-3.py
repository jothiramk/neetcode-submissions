class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        duplicate = set()
        #sample input nums = [1,2,3,1], k = 3
        for r, num in enumerate(nums):
            if num not in duplicate:
                duplicate.add(num)
            elif num in duplicate:
                return True
            if r - l  == k :
                duplicate.remove(nums[l])
                l = l + 1
        return False
                


            
            
        