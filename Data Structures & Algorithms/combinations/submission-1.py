class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        for mask in range(2**n):
            if mask.bit_count() != k:
                continue
            comb = [i + 1 for i in range(n) if (mask >> i) & 1 == 1]
            res.append(comb)
        return res                    