class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [(0, 0, 0)]
        eff_map = defaultdict(lambda: float("inf"))
        while heap:
            effort, i, j = heapq.heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return effort
            for (k, l) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= k < m) or not (0 <= l < n):
                    continue
                new_effort = max(effort, abs(heights[i][j] - heights[k][l]))
                if new_effort < eff_map[(k, l)]:
                    heapq.heappush(heap, (new_effort, k, l))
                    eff_map[(k, l)] = new_effort
        return -1