class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num%2 == 0:
                result.insert(0,num)
            else:
                result.append(num)
        return result
