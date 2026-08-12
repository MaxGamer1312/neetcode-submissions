class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        answer = 1
        mapOfPosition = {}
        for i in range(len(position)):
            mapOfPosition[position[i]] = speed[i]
        newPosition = sorted(position.copy())
        newSpeed = []
        for i in newPosition:
            newSpeed.append(mapOfPosition[i])
        highestAcceptableNumber = -1
        for i in range(len(newPosition)-2,-1,-1):
            solutionForIAfter = (target-newPosition[i+1])/newSpeed[i+1]
            if highestAcceptableNumber < solutionForIAfter:
                highestAcceptableNumber = solutionForIAfter
            if newSpeed[i]*highestAcceptableNumber + newPosition[i] < target:
                answer += 1
        return answer

        