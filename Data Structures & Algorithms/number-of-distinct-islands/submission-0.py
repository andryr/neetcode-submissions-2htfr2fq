class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        m, n = len(grid), len(grid[0])

        def get_island(i0, j0, i, j, island):
            nonlocal seen
            seen.add((i, j))
            island.append((i - i0, j - j0))
            for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (u, v) in seen or not (0 <= u < m) or not (0 <= v < n) or grid[u][v] != 1:
                    continue
                get_island(i0, j0, u, v, island)
            return island


        islands = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in seen:
                    continue
                if grid[i][j] == 1:
                    islands.add(tuple(get_island(i, j, i, j, [])))
        return len(islands)