class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        ans = 0
        num_fresh_fruits = len([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        while queue and num_fresh_fruits:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if not (0 <= k < m) or not (0 <= l < n) or grid[k][l] != 1:
                        continue
                    grid[k][l] = 2
                    queue.append((k, l))
                    num_fresh_fruits -= 1
            ans += 1
        return ans if num_fresh_fruits == 0 else -1