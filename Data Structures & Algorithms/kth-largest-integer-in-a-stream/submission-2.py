class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap,num)
            # print(self.min_heap[0])
            if len(self.min_heap)>k:
                # print(f'len i s{len(nums)}')
                heapq.heappop(self.min_heap)
                # print(f'after pop {self.min_heap[0]}')    
        # print('jothi')
        # while self.min_heap:
        #     print(f'popoing {heapq.heappop(self.min_heap)}')
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
