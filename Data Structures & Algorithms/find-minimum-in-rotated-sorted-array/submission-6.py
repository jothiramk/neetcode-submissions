class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the pivot is the first(min) element where the array is rotated
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m 
        
        return nums[l]