class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_servers_row = [0] * m
        num_servers_col = [0] * n
        num_servers = 0
        for i in range(m):
            for j in range(n):
                num_servers += grid[i][j]
                num_servers_row[i] += grid[i][j]
                num_servers_col[j] += grid[i][j]
        num_isolated = 0
        for i in range(m):
            for j in range(n):
                num_isolated += num_servers_row[i] == num_servers_col[j] == 1 == grid[i][j]
        return num_servers - num_isolated