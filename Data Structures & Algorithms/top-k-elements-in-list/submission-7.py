class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        result = []
        for num in nums:
            if num in freq_map:
                freq_map[num] =  (freq_map[num][0]+1,freq_map[num][1])
            else:
                freq_map[num] =  (1,num)
        
        list_value = list(freq_map.values())
        list_value.sort(reverse=True)
        # print(list_value)
        
        for i in range(k):
            result.append(list_value[i][1])

        return result