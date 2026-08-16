class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        unique_fleets = 0
        for i in range(len(position)):
            position[i] = [position[i], (target-position[i])/speed[i]]
        position.sort(key = lambda x: x[0], reverse = True)
        
        prev_time = -1
        for i in range(len(position)):
            if prev_time == -1 or position[i][1] > prev_time:
                prev_time = position[i][1]
                unique_fleets += 1
        return unique_fleets
