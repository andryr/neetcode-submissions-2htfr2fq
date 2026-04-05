class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq1 = Counter(s1)
        freq2 = {}
        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
            if freq1 == freq2:
                return True
        return False