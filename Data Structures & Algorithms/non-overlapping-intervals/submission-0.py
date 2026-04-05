class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_a, last_b = None, None
        ans = 0
        for a, b in intervals:
            if last_a and a < last_b:
                ans += 1
                if b < last_b:
                    last_a, last_b = a, b
            else:
                last_a, last_b = a, b
        return ans
        