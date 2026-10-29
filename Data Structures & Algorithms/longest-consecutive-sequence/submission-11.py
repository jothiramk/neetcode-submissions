class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        
        for num in numSet:
            #only process where num-1 is not in the set in the if
            if num-1 not in numSet:
                temp_res = 1
                curr = num
                seq_len = 1
                while curr+seq_len in numSet:
                    temp_res+=1
                    curr += seq_len
                res = max(res,temp_res)
        return res
