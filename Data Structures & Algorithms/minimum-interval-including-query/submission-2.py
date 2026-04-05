class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[1])
        sorted_idx = sorted(range(len(queries)), key=lambda i:queries[i])
        ans = [-1] * len(queries)
        i = 0
        for k in sorted_idx:
            q = queries[k]
            while i < len(intervals) and intervals[i][1] < q:
                i += 1
            shortest_len = float("inf")
            j = i
            while j < len(intervals) and q <= intervals[j][1]:
                if intervals[j][0] <= q:
                    shortest_len = min(intervals[j][1] - intervals[j][0] + 1, shortest_len)
                j += 1
            ans[k] = shortest_len if shortest_len < float("inf") else -1
        return ans