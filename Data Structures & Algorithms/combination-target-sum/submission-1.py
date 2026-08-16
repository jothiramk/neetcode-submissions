class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # Choose to include nums[i]:
            #     Add nums[i] to currentList
            #     Call dfs(i, currentList, total + nums[i]) (stay at same index)
            #     Remove nums[i] (backtrack)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # Choose to skip nums[i]:. 
            cur.pop()
           
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res