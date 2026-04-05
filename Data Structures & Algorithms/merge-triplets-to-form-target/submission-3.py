import bisect
import itertools
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        triplets = [(s, t, u) for s, t, u in triplets if s <= x and t <= y and u <= z]

        return any(s == x for s, t, u in triplets) and any(t == y for s, t, u in triplets) and any(u == z for s, t, u in triplets)
