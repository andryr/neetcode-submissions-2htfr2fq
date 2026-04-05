import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        cnt = {}
        l = 0
        max_f = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            max_f = max(max_f, cnt[s[r]])
            while r - l + 1 - max_f > k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans