class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums)-1
        
        while low <= high:
            
            mid = (low+high)//2
            print (f'low {low} high is {high} mid is {mid}')
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        
        return -1