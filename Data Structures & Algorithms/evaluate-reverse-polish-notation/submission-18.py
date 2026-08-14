class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            match token:
                case '+':
                    operands[len(operands) - 2] += operands.pop()
                case '-':
                    operands[len(operands) - 2] -= operands.pop()
                case '*':
                    operands[len(operands) - 2] *= operands.pop()
                case '/':
                    op1i = len(operands) - 2
                    operands[op1i] = int(operands[op1i] / operands.pop())
                case _:
                    operands.append(int(token))
        return operands[0]