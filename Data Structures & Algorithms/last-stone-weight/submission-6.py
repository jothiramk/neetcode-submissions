class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 - stone2 > 0:
                heapq.heappush_max(stones,(stone1 - stone2))
        
        return stones[0] if stones else 0