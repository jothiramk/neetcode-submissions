class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap=[]
        #create a custom heap a pair(dist, [x,y])
        for coordinates in points:
            x = coordinates[0]
            y = coordinates[1]
            euc_dist = math.sqrt((x-0)**2 + (y-0)**2)
            pair= (euc_dist,coordinates)
            heapq.heappush(min_heap,pair)
        res = []
        while k :
            res.append(heapq.heappop(min_heap)[1])
            k= k-1
        
        return res