from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = [0] + days
        n = len(days)
        dp = [0] * n
        for i in range(1, n):
            seven_idx = bisect_left(days, days[i] - 7)
            if days[seven_idx] > days[i] - 7:
                seven_idx -= 1
            thirty_idx = bisect_left(days, days[i] - 30)
            if days[thirty_idx] > days[i] - 30:
                thirty_idx -= 1
            dp[i] = min(dp[i - 1] + costs[0], dp[seven_idx] + costs[1], dp[thirty_idx] + costs[2])
        return dp[-1]



