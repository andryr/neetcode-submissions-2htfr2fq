class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for a, b in intervals:
            if ans:
                last_a, last_b = ans[-1]
                if last_a <= a <= last_b or a <= last_a <= b:
                    ans.pop()
                    ans.append([min(a, last_a), max(b, last_b)])
                else:
                    ans.append([a, b])
            else:
                ans.append([a, b])
        return ans