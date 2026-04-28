class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.matrix_sum = [[matrix[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0:
                    self.matrix_sum[i][j] += self.matrix_sum[i - 1][j]
                if j > 0:
                    self.matrix_sum[i][j] += self.matrix_sum[i][j - 1]
                if i > 0 and j > 0:
                    self.matrix_sum[i][j] -= self.matrix_sum[i - 1][j - 1]





    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.matrix_sum[row2][col2]
        if row1 > 0:
            res -= self.matrix_sum[row1 - 1][col2]
        if col1 > 0:
            res -= self.matrix_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.matrix_sum[row1 - 1][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)