class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.arr.append(val)
        self.val_to_idx[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        if idx < len(self.arr) - 1:
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            self.val_to_idx[self.arr[idx]] = idx
        self.arr.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        idx = random.randrange(len(self.arr))
        return self.arr[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()