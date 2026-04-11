class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for k in range(0, limit + 1):
            hi = min(limit, n - k)
            lo = max(0, n - k - limit)
            if hi >= lo:
                ans += hi - lo + 1
        return ans