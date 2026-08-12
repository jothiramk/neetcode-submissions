class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t or not s:
            return True
        if len(t) < len(s):
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j+=1
            else:
                if i == len(s)-1:
                    return True
                i+=1
                j+=1
                
        return False

                
