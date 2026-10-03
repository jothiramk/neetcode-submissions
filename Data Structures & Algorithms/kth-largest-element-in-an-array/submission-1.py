class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush_max(max_heap,num)
        
        top = 0
        while k :
            top = heapq.heappop_max(max_heap)
            k -=1
        
        return top