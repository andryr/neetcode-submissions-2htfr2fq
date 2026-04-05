class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for a, b in intervals:
            last_b = ans[-1][1]
            if a <= last_b:
                ans[-1][1] = max(b, last_b)
            else:
                ans.append([a, b])
        return ans