class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l = 0
        h = len(nums)-1

        while l < h :
            
            m = (l+h)//2
            print(f'l is {l} and h is {h} and m is {m}')
            #min element is in the right side
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        return nums[l]