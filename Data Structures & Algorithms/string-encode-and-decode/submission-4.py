class Solution:
    def __init__(self):
        self.delimeter = '#'
        
    def encode(self, strs: List[str]) -> str:
        result = ''
        # delimeter = '#'
        for word in strs:
            size = len(word)
            result +=  str(size) + self.delimeter + word
        # print (result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        size = len(s)
        
        while i < size:
            numb = ''
            while i < size and s[i].isdigit():
                numb += s[i]
                i+=1
            # delimeter is at index i now.
           
            result.append(s[i+1:i+1+int(numb)])
           
            i+=int(numb)+1

        return result