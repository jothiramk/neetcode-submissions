class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        resStartIndex=0
        resLen =0
        
        for i in range(size):
            #for odd length
            l, r = i, i
            while l>=0 and r<size and (s[l] == s[r]):
                #need to calculate lenght of substring to see if it is bigger then the prior substring
                if (r - l +1) > resLen:
                    resStartIndex = l
                    resLen = r - l + 1
                l-=1
                r+=1
                
            #for even size strings
            l, r = i, i+1
            while l>=0 and r<size and (s[l] == s[r]):
                if (r - l +1) > resLen:
                    resStartIndex = l
                    resLen = r - l + 1
                l-=1
                r+=1
        return s[resStartIndex : resStartIndex + resLen]