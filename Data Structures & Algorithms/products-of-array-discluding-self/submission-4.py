class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_prd = [1] * size
        suffix_prd = [1] * size

        for i in range(1,size):
            prefix_prd[i] = prefix_prd[i-1]*nums[i-1]

        for j in range(size-2,-1,-1):
            suffix_prd[j] = suffix_prd[j+1] * nums[j+1]

        # print(f'pre is {prefix_prd} and {suffix_prd}')
        res = []
        for pre,suf in zip(prefix_prd,suffix_prd):
            res.append(pre*suf)
        
        return res