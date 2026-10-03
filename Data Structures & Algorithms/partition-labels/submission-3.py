class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_tracker = defaultdict(str)
        result = []
        for i,ch in enumerate(s):
            index_tracker[ch] = i
        
        size = 0
        last_index =0
        for i, ch in enumerate(s):
            size+=1
            last_index = max(last_index,index_tracker[ch])
            if i == last_index:
                result.append(size)
                size = 0
        return result 
        
            
        
