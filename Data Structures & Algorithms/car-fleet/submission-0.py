class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        print(cars)

        fleet, prev = 0, 0 
        for i, value in enumerate(cars):
            position, speed = value
            print(position)
            time = (target - position) / speed
            if time > prev:
                fleet += 1
                prev = time
        
        return fleet