class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    
    def pop(self) -> None:
        if not self.stack:
            return
        result =   self.min - self.stack[-1]
        if self.stack.pop() < 0:
            self.min = result
        

    def top(self) -> int:
        if not self.stack:
            return 
        top = self.stack[-1]
        if top >= 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
