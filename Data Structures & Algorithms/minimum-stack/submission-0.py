class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.Min[-1] if self.Min else val)
        self.Min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.Min[-1]
