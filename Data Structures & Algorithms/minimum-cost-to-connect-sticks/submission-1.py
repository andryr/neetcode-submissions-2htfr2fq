class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2:
            return 0
        heap = sticks[::]
        heapq.heapify(heap)
        ans = 0
        while len(heap) > 1:
            cur = heapq.heappop(heap) + heapq.heappop(heap)
            heapq.heappush(heap, cur)
            ans += cur
        return ans
