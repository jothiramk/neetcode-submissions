class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_count = {}
        for i in range(len(s)):
            if s[i] in ch_count:
                ch_count[s[i]]+=1
            else:
                ch_count[s[i]] = 1
        print(f"dict value is {ch_count}")
        for k in range(len(t)):
            if t[k] in ch_count and ch_count[t[k]]!=0:
                ch_count[t[k]] -=1
            else:
                return False
        
        return True