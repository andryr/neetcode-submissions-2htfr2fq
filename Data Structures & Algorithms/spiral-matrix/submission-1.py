class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_direction_idx = 0

        ans = []
        cur_cell = (0, 0)
        visited = set()
        for k in range(m * n):
            i, j = cur_cell
            visited.add((i, j))
            ans.append(matrix[i][j])
            di, dj = directions[cur_direction_idx]
            new_i, new_j = (i + di, j + dj)
            if not (0 <= new_i < m) or not (0 <= new_j < n) or (new_i, new_j) in visited:
                cur_direction_idx = (cur_direction_idx + 1) % 4
                di, dj = directions[cur_direction_idx]
                new_i, new_j = (i + di, j + dj)
            cur_cell = (new_i, new_j)
        return ans
