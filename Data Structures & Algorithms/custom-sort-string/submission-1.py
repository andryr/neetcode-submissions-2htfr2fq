class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []
        for c in order:
            while freq[c]:
                res.append(c)
                freq[c] -= 1
        for c in freq:
            while freq[c]:
                res.append(c)
                freq[c] -= 1
        return "".join(res)