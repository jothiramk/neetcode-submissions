class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position,speed)
        cars_order = sorted(cars,reverse=True)
        

        fleet = 0
        time = -math.inf
        for car in cars_order:
            pos = car[0]
            speed = car[1]
            travel_time = (target - pos)/speed
            if travel_time > time:
                fleet+=1
                time = travel_time
            
        return fleet