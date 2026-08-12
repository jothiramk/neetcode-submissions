class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        j = size - 1
        res = 0
        word_found = False
        while j >= 0:
            # print (f'j is {j} and s[j] is {s[j]}')
            if not word_found and not s[j].isalpha():
                j-=1
                continue
            elif word_found and not s[j].isalpha():
                return res
            else:
                res+=1
                word_found = True
            j-=1
        return res
            
