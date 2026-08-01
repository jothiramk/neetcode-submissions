class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_prod = 1
        for num in nums:
            full_prod *= num
        res = []
        for i, num in enumerate(nums):
            if num == 0 :
                value = 1
                for j,num in enumerate(nums):
                    if j == i:
                        continue
                    else:
                        value *= num
                res.append(value)
            else:
                res.append(int(full_prod/num))
        return res
            