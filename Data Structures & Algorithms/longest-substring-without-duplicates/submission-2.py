class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        sub_str = set()
        for r in range(len(s)):
            if s[r] not in sub_str:
                sub_str.add(s[r])
                res = max(res,r-l+1)
                # print(f'{sub_str} and {res} and r index {r} and l index {l}')
            else:
                while (s[r] in sub_str):
                    # print(s[l])
                    sub_str.remove(s[l])
                    l = l+1
                sub_str.add(s[r])
        return res            
        

