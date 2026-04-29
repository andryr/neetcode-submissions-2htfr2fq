class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for center in range(n):
            ans += 1
            for i in range(1, n):
                if not (0 <= center - i <= center + i < n) or s[center - i] != s[center + i]:
                    break
                ans += 1
            for i in range(1, n):
                if not (0 <= center - i + 1 <= center + i < n) or s[center - i + 1] != s[center + i]:
                    break
                ans += 1
        return ans
                