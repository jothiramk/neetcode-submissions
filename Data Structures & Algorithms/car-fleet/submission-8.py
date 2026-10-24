class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_list = []
        for pos,speed in zip(position,speed):
            pos_speed_list.append((pos,speed))
        pos_speed_list.sort(reverse=True)
        # print(pos_speed_list)

        first_car = pos_speed_list[0]
        target_time = float((target-first_car[0])/first_car[1])
        # print(f'target_time is {target_time}')
        fleet = 1
        for i in range(1,len(pos_speed_list)):
            pos, speed = pos_speed_list[i]
            time = float((target-pos)/speed)
            # print(f'candidate time  is {time}')
            if time > target_time:
                fleet+=1
                target_time = time


        return fleet