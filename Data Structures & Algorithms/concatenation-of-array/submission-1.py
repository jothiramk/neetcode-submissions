class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums + nums
        # ans.extend([num for num in nums])
        return ans