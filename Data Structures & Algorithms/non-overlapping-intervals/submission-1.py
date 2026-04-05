class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_b = None
        ans = 0
        for a, b in intervals:
            if last_b and a < last_b:
                ans += 1
                if b < last_b:
                    last_b = b
            else:
                last_b = b
        return ans
        