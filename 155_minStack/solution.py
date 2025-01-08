"""
MinStack - stack that also provides the minimal element
push, pop, top, getmin - all functions O(1)"""


class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.minStack: list[int] = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val < self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None
        
