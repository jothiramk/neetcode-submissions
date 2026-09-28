class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charLastIndex = {}
        for i,ch in enumerate(s):
            charLastIndex[ch] = i
        
        # for key,value in charLastIndex.items():
        #     print(f'{key} and last index {value}')

        
        size = 0
        end = 0
        res = []
        for i,ch in enumerate(s):    
            size +=1   
            end = max(end,charLastIndex[ch])
            if i == end:
                res.append(size)
                size = 0
            
        
        return res

    