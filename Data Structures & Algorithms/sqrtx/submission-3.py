class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            m = (l + r) // 2
            sq = m * m
            if sq == x:
                return m
            elif sq < x:
                l = m + 1
            else:
                r = m - 1
        return l if l * l <= x else l - 1