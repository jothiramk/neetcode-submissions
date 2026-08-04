class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest_time = 0
        for pos,mph in sorted(zip(position,speed),reverse=True):
            time = (target-pos)/mph
            # print (f'{pos} {mph} {time} {slowest_time}')
            if time > slowest_time:
                slowest_time = time
                fleets += 1
            
        return fleets