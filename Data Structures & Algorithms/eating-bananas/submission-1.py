class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        hrs = math.inf
        while l <= r:
            k = (l+r)//2
            print(f'l is {l} and r is {r} and k is {k}')
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            print(f'total time is {time}')
            if time <= h:
                res = k
                r = k -1
            else:
                l = k + 1
        return res
