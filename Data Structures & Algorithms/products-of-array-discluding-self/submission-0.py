class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i  = 0 
        size = len(nums)
        while i < size:
            value = 1
            for j,num in enumerate(nums):
                if i == j:
                    continue
                else:
                    value *= num
            res.append(value)
            # print(res)
            i+=1
        return res