class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums):
            if i == len(nums):
                return [[]]
            
            resperms = []
            perms = helper(i+1,nums)
            for p in perms:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j,nums[i])
                    resperms.append(pcopy)
            return resperms

        
        return helper(0,nums)

        