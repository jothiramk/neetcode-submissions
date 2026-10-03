class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        for num in nums:            
            if len(self.min_heap)>=k:
                if num < self.min_heap[0]:
                    continue
                heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap,num)
        self.k = k
        

    def add(self, val: int) -> int:

        if len(self.min_heap)>=self.k:
            if val < self.min_heap[0]:
                return self.min_heap[0]
            heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap,val)
        return self.min_heap[0]
            
