class Solution:
    def helper (self, l: int, r: int,size : int,s: str):
        res = 0
        while l>=0 and r < size and s[l]==s[r]:
            res+=1
            l = l-1
            r = r+1
        return res
    def countSubstrings(self, s: str) -> int:
        res = 0
        size = len(s)

        for i in range(size):
            #odd size palindromes
            res += self.helper(i,i,size,s)
            
            #even size palindromes
            res += self.helper(i,i+1,size,s)
            

        return res