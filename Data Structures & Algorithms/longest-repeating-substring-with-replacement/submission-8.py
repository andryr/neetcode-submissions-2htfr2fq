import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        for letter in string.ascii_uppercase:
            rep = 0
            l, r = 0, 0
            while r < len(s):
                if s[r] == letter or rep < k:
                    ans = max(ans, r - l + 1)
                if s[r] != letter:
                    if rep == k:
                        while s[l] == letter:
                            l += 1
                        l += 1
                        rep -= 1
                    else:
                        rep += 1
                        r += 1
                else:
                    r += 1
        return ans