class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        heap = []
        for key, val in freq.items():
            pair = (-val,key)
            heapq.heappush(heap,pair)
            # print(pair)
        
        res = []
        heap_len = len(heap)
        while heap:
            top = heapq.heappop(heap)
            # print(f'top is {top}')
            res.append(top[1])
            if len(res) == k:
                break
        
        return res