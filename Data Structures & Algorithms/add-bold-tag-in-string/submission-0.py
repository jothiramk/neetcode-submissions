class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        for word in words:
            
            index = s.find(word)
            # print(f'word is {word} and {index}')
            while index != -1:
                for i in range(index, index+len(word)):
                    bold[i] = True
                index = s.find(word,index+1)
        
        # print(bold)
        
        openTag = '<b>'
        closeTag = '</b>'
        ans = []
        for i in range(len(s)):
            if bold[i] and (i ==0 or bold[i-1]!= True):
                ans.append(openTag)
            
            ans.append(s[i])

            if bold[i] and (i == n-1 or bold[i+1] != True):
                ans.append(closeTag)
            
        return "".join(ans)

        