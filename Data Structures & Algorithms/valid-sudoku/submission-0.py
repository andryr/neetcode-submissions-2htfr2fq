class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            cnt = Counter(row)
            if any(cnt[str(i)] > 1 for i in range(1, 10)):
                return False
        
        for j in range(9):
            cnt = Counter([board[i][j] for i in range(9)])
            if any(cnt[str(i)] > 1 for i in range(1, 10)):
                return False
        
        for k in range(9):
            itl, jtl = k // 3 * 3, k % 3 * 3
            ibr, jbr = itl + 3, jtl + 3  
            cnt = Counter([board[i][j] for i in range(itl, ibr) for j in range(jtl, jbr)])
            if any(cnt[str(i)] > 1 for i in range(1, 10)):
                return False
        return True