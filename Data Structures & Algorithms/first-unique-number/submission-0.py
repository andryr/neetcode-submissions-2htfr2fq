class FirstUnique:

    def __init__(self, nums: List[int]):
        cnt = Counter(nums)
        self.queue = deque([num for num in nums if cnt[num] == 1])
        self.seen = set(self.queue)
        self.to_delete = set()


    def showFirstUnique(self) -> int:
        while self.queue and self.queue[0] in self.to_delete:
            self.to_delete.remove(self.queue[0])
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def add(self, value: int) -> None:            
        if value in self.seen:
            self.to_delete.add(value)
        else:
            self.queue.append(value)
            self.seen.add(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
