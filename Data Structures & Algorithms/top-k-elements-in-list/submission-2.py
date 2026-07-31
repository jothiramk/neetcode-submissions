class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
 # I have used max heap here, check the solution where they have used min heap
        for num in nums:
            freq[num] += 1
        heap = []
        for key, val in freq.items():
            pair = (-val,key)
            heapq.heappush(heap,(-val,key))
        
        res = []
        while k:
            top = heapq.heappop(heap)
            res.append(top[1])
            k-=1
        
        return res