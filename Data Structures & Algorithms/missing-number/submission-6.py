class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #assuming sorted list
        
        nums.sort()
        #n is the number of integers in the list, so if n is 3 there
        n = nums[-1]
        for i in range(n):
            print(f'i is {i} and nums[i] is {nums[i]}')
            if i != nums[i]:
                return i
        
        return n+1


    
