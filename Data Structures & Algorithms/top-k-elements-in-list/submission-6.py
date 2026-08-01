class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res= []
        # for num in nums:
        #     heapq.heappush(max_heap,-num)
        # print (f'max_heap is {max_heap}')
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        print (f'counter is {counter}')
        for key,value in counter.items():
            heapq.heappush(max_heap,(-value,key))
        
        print(max_heap)
        while max_heap:
            value = heapq.heappop(max_heap)
            res.append(value[1])
            if len(res) == k:
                return res

        return res

        
 