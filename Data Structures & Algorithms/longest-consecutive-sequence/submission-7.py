class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        result = 0
        nums.sort()
        count = 0
        i = 0
        print(nums)
        for j in range(i+1, len(nums)):
            # print(f'begining value of {i} and {j}')
            if nums[j]==nums[j-1]:
                # j+=1
                # print(f'duplicate incrementing {j}')
                continue
            if nums[j]-nums[i]==1:              
                count +=1
                result=max(result,count)
                # print(f'its a match {nums[j]} and {nums[i]} and count {count} and {result} ')
                i = j
                # print(f'value of {i} and {j}')
            else:
                # print(f'reseting count {nums[j]} and {nums[i]}')
                count = 0
                i = j
                
        
        return result+1
        