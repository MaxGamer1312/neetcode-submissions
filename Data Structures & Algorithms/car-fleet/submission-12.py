class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapOfPosition = {}
        for i in range(len(position)):
            mapOfPosition[position[i]] = speed[i]
        newPosition = sorted(position.copy())
        newSpeed = []
        for i in newPosition:
            newSpeed.append(mapOfPosition[i])

        stack = []
        stack.append((target-newPosition[-1])/newSpeed[-1])
        for i in range(len(newPosition)-2,-1,-1):
            stack.append((target-newPosition[i])/newSpeed[i])
            if stack[len(stack)-1] <= stack[len(stack)-2]:
                stack.pop()

        return len(stack)

        