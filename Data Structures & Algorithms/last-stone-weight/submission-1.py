class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #i'll have to create a max heap
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap,-stone)

        while len(max_heap)>1:
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)

            if first_stone == second_stone:
                continue
            else:
                new_val = first_stone - second_stone
                heapq.heappush(max_heap,-new_val)
        
        return -max_heap[0] if max_heap else 0
