class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 0])
        while queue:
            i, j, d = queue.popleft()
            for k, l in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= k < m) or not (0 <= l < n) or grid[k][l] < INF:
                    continue
                grid[k][l] = d + 1
                queue.append((k, l, d + 1))

