class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #build a max heap
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap,-num)
        res = -1
        while k:
            res = heapq.heappop(max_heap)
            k= k - 1
        
        return -res