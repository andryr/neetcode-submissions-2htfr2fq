import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        for letter in string.ascii_uppercase:
            cnt = 0
            l = 0
            for r in range(len(s)):
                if s[r] == letter:
                    cnt += 1
                
                while r - l + 1 - cnt > k:
                    if s[l] == letter:
                        cnt -= 1
                    l += 1
                ans = max(ans, r - l + 1)
        return ans