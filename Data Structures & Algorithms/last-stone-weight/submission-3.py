class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #negate stone to create a max heap
        max_heap = []
        for stone in stones:
            max_heap.append(-stone)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # top = -max_heap[0]
            top = -heapq.heappop(max_heap)
            second_top = -heapq.heappop(max_heap)
            # print(f' top is {top} and {second_top}' )
            if top == second_top:
                continue
            diff =  top - second_top            
            heapq.heappush(max_heap,-diff)


        return -max_heap[0] if max_heap else 0
