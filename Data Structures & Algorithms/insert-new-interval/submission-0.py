import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        all_intervals = [[a, b] for a, b in intervals]
        idx = bisect.bisect(all_intervals, newInterval, key=lambda x:[x[0],x[1]])
        all_intervals.insert(idx, newInterval)
        ans = []
        for a, b in all_intervals:
            if ans:
                last_a, last_b = ans[-1]
                if a <= last_a <= b or last_a <= a <= last_b:
                    ans.pop()
                    ans.append([min(a, last_a), max(b, last_b)])
                else:
                    ans.append([a, b])
            else:
                ans.append([a, b])
        return ans
        

