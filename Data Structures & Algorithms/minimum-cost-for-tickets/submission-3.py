from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = [0] + days
        n = len(days)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = float("inf")
            j = i
            for d, c in zip([1, 7, 30], costs):
                while j > 0 and days[j] > days[i] - d:
                    j -= 1
                dp[i] = min(dp[i], dp[j] + c)
        return dp[-1]



