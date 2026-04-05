class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = None
        l = 0
        tfreq = Counter(t)
        sfreq = {}
        ans_l, ans_r = 0, len(s) - 1
        for r in range(len(s)): 
            sfreq[s[r]] = sfreq.get(s[r], 0) + 1
            while all([sfreq.get(l, 0) >= tfreq[l] for l in tfreq]):
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r 
                sfreq[s[l]] -= 1
                l += 1
        ans = s[ans_l:ans_r + 1]
        sfreq = Counter(ans)
        if not all([sfreq.get(l, 0) >= tfreq[l] for l in tfreq]):
            return ""
        else:
            return ans