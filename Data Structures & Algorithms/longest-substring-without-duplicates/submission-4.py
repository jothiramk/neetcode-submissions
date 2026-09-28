class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        window = set()
        res = 0

        for r in range(len(s)):
            #shrink the window
            while s[r] in window:
                window.remove(s[l])
                # print(f'removing window is {window} ')
                l+=1
            
            window.add(s[r])
            res = max (res, r-l+1)
            # print(f'window is {window} and {res}')
        
        return res
