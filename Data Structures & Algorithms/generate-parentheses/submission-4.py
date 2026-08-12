class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        tempAnswer = [["(",1,0]]
        while len(tempAnswer) != 0:
            element = tempAnswer[len(tempAnswer) - 1].copy()
            nextList = []    
            oneFound = False
            print(tempAnswer)
            print(element[0] + ')') 
            if element[1] < n:
                print("one")
                tempAnswer[len(tempAnswer) - 1][0] += '('
                tempAnswer[len(tempAnswer) - 1][1] += 1
                oneFound = True
            if element[2] < n and element[1] - element[2] > 0:
                print("two")
                if oneFound:
                    nextList.append(element[0] + ')')
                    nextList.append(element[1])
                    nextList.append(element[2] + 1)
                    tempAnswer.append(nextList)
                else:
                    tempAnswer[len(tempAnswer) - 1][0] += ')'
                    tempAnswer[len(tempAnswer) - 1][2] += 1
                    oneFound = True
            if not oneFound:
                print("hi")
                answer.append(tempAnswer.pop()[0])
        return answer
                    

