class MinStack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, val: int) -> None:
        self.stack_1.append(val)
        min_elt = self.stack_2[-1] if self.stack_2 else float("inf")
        self.stack_2.append(min(min_elt, val))

    def pop(self) -> None:
        self.stack_1.pop()
        self.stack_2.pop()
        

    def top(self) -> int:
       return self.stack_1[-1] 

    def getMin(self) -> int:
        return self.stack_2[-1]
        
