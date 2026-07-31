class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        heap = []
        for key, val in freq.items():
            pair = (-val,key)
            heapq.heappush(heap,pair)
        
        res = []
        heap_len = len(heap)
        while k:
            top = heapq.heappop(heap)
            res.append(top[1])
            # if len(res) == k:
            #     break
            k-=1
        
        return res