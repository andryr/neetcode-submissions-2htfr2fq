class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def mark_island(i, j):
            grid[i][j] = '0'
            for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if not (0 <= k < m) or not (0 <= l < n) or grid[k][l] != '1':
                    continue
                mark_island(k, l)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    mark_island(i, j)
        return ans
