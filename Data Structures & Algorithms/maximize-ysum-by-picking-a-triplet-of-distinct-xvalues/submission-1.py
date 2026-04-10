class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        x_to_y = defaultdict(int)
        for x_val, y_val in zip(x, y):
            x_to_y[x_val] = max(y_val, x_to_y[x_val])
        y = x_to_y.values()
        if len(y) < 3:
            return -1
        heap = []
        for y_val in y:
            heapq.heappush(heap, y_val)
            if len(heap) > 3:
                heapq.heappop(heap)
        return sum(heap)