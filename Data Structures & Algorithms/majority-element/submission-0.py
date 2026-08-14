class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = -float("inf")
        result_key = 0
        for key in count:
            if count[key] > res:
                res=count[key]
                result_key = key
        
        return result_key