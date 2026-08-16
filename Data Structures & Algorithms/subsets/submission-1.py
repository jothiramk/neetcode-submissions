class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subsets = []
            for sub_set in res:
                new_subsets.append(sub_set + [num])
            res.extend(new_subsets)

        return res