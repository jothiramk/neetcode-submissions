class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            first_stone = heapq.heappop_max(max_heap)
            second_stone = heapq.heappop_max(max_heap)
            if first_stone - second_stone  == 0:
                continue
            else:
                heapq.heappush_max(max_heap,abs(first_stone-second_stone))

        return max_heap[0] if len(max_heap) >0 else 0
