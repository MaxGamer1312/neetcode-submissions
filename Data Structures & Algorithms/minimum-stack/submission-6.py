class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixMinStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefixMinStack) == 0 or val < self.prefixMinStack[len(self.prefixMinStack) - 1]:
            self.prefixMinStack.append(val)
        else:
            self.prefixMinStack.append(self.prefixMinStack[len(self.prefixMinStack) - 1])
        
    def pop(self) -> None:
        self.stack.pop()
        self.prefixMinStack.pop()
        
    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.prefixMinStack[len(self.prefixMinStack) - 1]
    
        
