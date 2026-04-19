class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        min_heap = []
        for i in range(len(temperatures) - 1, -1, -1):
            while min_heap and min_heap[0][0] <= temperatures[i]:
                heapq.heappop(min_heap)
            if min_heap:
                result[i] = min_heap[0][1] - i
            heapq.heappush(min_heap, (temperatures[i], i))
        return result