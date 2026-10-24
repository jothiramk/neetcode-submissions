class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap,(dist,[x,y]))
        
        res = []
        while k > 0:
            dist, coordinate = heapq.heappop(heap)
            res.append(coordinate)
            k-=1
        return res
