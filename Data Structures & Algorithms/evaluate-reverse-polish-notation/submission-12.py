class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            else:
                
                op2 = stack.pop()
                op1 = stack.pop()
                match i:
                    case '+':
                        stack.append(op1 + op2)
                    case '-':
                        stack.append(op1 - op2)
                    case '*':
                        stack.append(op1 * op2)
                    case '/':
                        stack.append(int(op1 / op2))
                    case _:
                        print(i.isdigit())
            print(stack)
        return stack[0]