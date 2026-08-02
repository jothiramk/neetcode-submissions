class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          
        numset = set(nums)
        res = 0
        for num in numset:
            if num-1 not in numset:
                # beginning of a sequence 
                print(f'seq beg number is {num}')
                curr = num
                length_seq = 1
                while curr + length_seq in numset:
                    length_seq += 1
                res = max(length_seq,res)    
    
        return res