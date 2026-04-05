class MinStack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, val: int) -> None:
        self.stack_1.append(val)
        if self.stack_2:
            self.stack_2.append(min(val, self.stack_2[-1]))
        else:
            self.stack_2.append(val)
    def pop(self) -> None:
        self.stack_1.pop()
        self.stack_2.pop()

    def top(self) -> int:
        return self.stack_1[-1]

    def getMin(self) -> int:
        return self.stack_2[-1]
