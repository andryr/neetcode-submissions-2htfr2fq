class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i + j >= n:
                    continue
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]
        
        for i in range(n):
            if i >= n // 2:
                continue
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

