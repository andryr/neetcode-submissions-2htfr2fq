import bisect

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        arr = self.map[key]
        idx = bisect.bisect(arr, timestamp, key=lambda x:x[0])
        if idx > 0:
            return arr[idx - 1][1]
        else:
            return ""
        
