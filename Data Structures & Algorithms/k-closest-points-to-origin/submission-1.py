class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        result = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(max_heap,(-dist,point))
            if len(max_heap) > k :
                heapq.heappop(max_heap)

        while max_heap:
            point = heapq.heappop(max_heap)
            result.append(point[1])

        return result
