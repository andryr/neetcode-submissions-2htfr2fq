class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[i == j for j in range(n)] for i in range(n)]
        res_i, res_len = 0, 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_len = j - i + 1
                        res_i = i
                    
        return s[res_i:res_i + res_len]