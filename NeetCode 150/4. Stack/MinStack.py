class MinStack:
    def __init__(self):
        self.stack = []
        self.minv = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minv:
            minval = val
        else:
            minval = min(self.minv[-1], val)
        self.minv.append(minval)

    def pop(self) -> None:
        self.stack.pop()
        self.minv.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minv[-1]