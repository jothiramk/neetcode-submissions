class Solution:
    def dfs(self,i,subset,curset,nums):
        if i >= len(nums):
            temp_set = sorted(curset.copy())
            if temp_set not in subset:
                subset.append(temp_set)
            return
        
        curset.append(nums[i])
        self.dfs(i+1,subset,curset,nums)
        
        curset.pop()
        self.dfs(i+1,subset,curset,nums)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        curset = []

        self.dfs(0,subset,curset,nums)
        return subset
        