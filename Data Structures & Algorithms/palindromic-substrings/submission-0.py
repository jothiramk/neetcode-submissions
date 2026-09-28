class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        size = len(s)

        for i in range(size):
            #odd size palindromes
            l, r = i, i
            while l>=0 and r < size and s[l]==s[r]:
                res+=1
                l = l-1
                r = r+1

            #even size palindromes
            l, r = i, i+1
            while l>=0 and r < size and s[l]==s[r]:
                res+=1
                l = l-1
                r = r+1

        return res