class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_idx = sorted(range(len(queries)), key=lambda i:queries[i])
        ans = [-1] * len(queries)
        min_heap = []
        i = 0
        for k in sorted_idx:
            q = queries[k]
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            print(q, min_heap)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            ans[k] = min_heap[0][0] if min_heap else -1
        return ans