class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charLastIndex = {}
        for i,ch in enumerate(s):
            charLastIndex[ch] = i
        
        # for key,value in charLastIndex.items():
        #     print(f'{key} and last index {value}')

        
        start = 0
        end = 0
        res = []
        first = 0
        for i,ch in enumerate(s):    
            end = max(end,charLastIndex[ch])
            # print(f' processing index {i} and ch {ch} and {charLastIndex[ch]} and start is {start} end is {end}')
            if start == end:
                res.append(end+1-first)
                # print(f'storing first result {res}')
                first = i+1
            start +=1   
        
        return res

        

        return []