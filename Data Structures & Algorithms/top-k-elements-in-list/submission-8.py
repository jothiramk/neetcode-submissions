class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_heap = []
        for num,value in counter.items():
            heapq.heappush_max(max_heap,(value,num))
        res = []
        while k > 0:
            value, num = heapq.heappop_max(max_heap)
            res.append(num)
            k-=1
        
        return res
