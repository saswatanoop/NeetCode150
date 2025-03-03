
from typing import List

# 6. https://leetcode.com/problems/car-fleet/
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # T:O(nlogn) and S:O(n)
    # Sort the cars based on their position, and calculate the time required to reach target,from end and not from the start.
    # first car might not reach second carbut third car can block second car, so first can reach the second and third car
    car_pos_speed=[[x,v] for x,v in zip(position,speed)]
    car_pos_speed.sort(key=lambda x: x[0],reverse=True)
    time_queue=[]

    for car in car_pos_speed:
        time_required=(target-car[0])/car[1]
        if not time_queue or time_queue[-1]<time_required:
            time_queue.append(time_required)
    
    return len(time_queue)