class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_servers_row = [sum(row) for row in grid]
        num_servers_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        num_isolated = sum(num_servers_row[i] == num_servers_col[j] == 1 == grid[i][j] for i in range(m) for j in range(n))
        num_servers = sum(grid[i][j] for i in range(m) for j in range(n))
        return num_servers - num_isolated