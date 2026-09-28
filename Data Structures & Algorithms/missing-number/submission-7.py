class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        numbers = []
        for i in range(size+1):
            numbers.append(i)
        print(numbers)
        for i in range(size+1):
            if  numbers[i] not in nums:
                return numbers[i]
        
        return numbers[-1]
