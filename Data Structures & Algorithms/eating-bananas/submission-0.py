class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(piles, k, h):
            return sum(math.ceil(pile / k) for pile in piles) <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_eat(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1
        return lo
        