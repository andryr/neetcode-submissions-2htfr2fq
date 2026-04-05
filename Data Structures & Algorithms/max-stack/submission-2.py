class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []

        self.del_from_stack = set()
        self.del_from_heap = set()

    def push(self, x: int) -> None:
        self._lazy_remove_from_stack()
        self._lazy_remove_from_heap()

        self.stack.append(x)
        heapq.heappush_max(self.heap, x)

    def _lazy_remove_from_stack(self):
        while self.stack and self.stack[-1] in self.del_from_stack:
            self.del_from_stack.remove(self.stack[-1])
            self.stack.pop()
    
    def _lazy_remove_from_heap(self):
        while self.heap and self.heap[0] in self.del_from_heap:
            self.del_from_heap.remove(self.heap[0])
            heapq.heappop_max(self.heap)

    def pop(self) -> int:
        self._lazy_remove_from_stack()
        self.del_from_heap.add(self.stack[-1])
        return self.stack.pop()


    def top(self) -> int:
        self._lazy_remove_from_stack()
        return self.stack[-1]

    def peekMax(self) -> int:
        self._lazy_remove_from_heap()
        return self.heap[0]

    def popMax(self) -> int:
        self._lazy_remove_from_heap()
        self.del_from_stack.add(self.heap[0])
        return heapq.heappop_max(self.heap)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
