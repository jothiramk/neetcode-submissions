class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = [0] * len(nums)

        for num in nums:
            seen[num-1]+=1
        
        for num in seen:
            if num == 2:
                repeated_num = seen.index(num)+1
            elif num == 0:
                missing_num = seen.index(num)+1
            
        return [repeated_num,missing_num]