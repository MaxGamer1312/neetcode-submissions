class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        unfinished_temps = []
        for i, temperature in enumerate(temperatures):
            result.append(0)
            while unfinished_temps and temperature > temperatures[unfinished_temps[-1]]:
                result[unfinished_temps[-1]] = i-unfinished_temps[-1]
                unfinished_temps.pop()
            unfinished_temps.append(i)
        return result