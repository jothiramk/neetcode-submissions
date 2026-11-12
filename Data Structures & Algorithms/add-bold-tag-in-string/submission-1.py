class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        size = len(s)
        
        bold = [0] * size
        
        for word in words:
            index = s.find(word,0)
            while index != -1:
                for j in range(index, index+len(word)):                    
                    bold[j] = 1
                index = s.find(word,index+1)
                
                
        result = []
        for i in range (len(bold)):
            if bold[i] and (i == 0 or bold[i-1] == 0):
                result.append('<b>')
            result.append(s[i])
            if bold[i] and (i == size-1 or bold[i+1] == 0):
                result.append('</b>')
            

        return "".join(result)


