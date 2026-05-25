class MinStack:

    def __init__(self):
        self.stack = []
        self.sstack = []
        self.curmin = math.inf
        # second stack -> My top is ALWAYS the min value for the current first stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.curmin = min(self.curmin, val)
        self.sstack.append(self.curmin)

    def pop(self) -> None:
        self.stack.pop()
        self.sstack.pop()
        self.curmin = self.sstack[-1] if self.sstack else math.inf

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curmin # O(N)
