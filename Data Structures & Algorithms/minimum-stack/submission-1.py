class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min:
            val = min(self.current_min[-1], val)
        self.current_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.current_min.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]
