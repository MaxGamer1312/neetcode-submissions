class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        tempStack = []
        for i,tempValue in enumerate(temperatures):
            while len(tempStack) != 0 and tempValue > tempStack[len(tempStack) - 1][0]:
                lastElement = tempStack.pop()
                answer[lastElement[1]] = i - lastElement[1]

            tempStack.append([tempValue,i])

        return answer