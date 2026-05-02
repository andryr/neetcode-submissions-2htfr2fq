class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(cnt, c) for c, cnt in Counter(s).items()]
        heapq.heapify_max(heap)
        ans = []

        while heap:
            cnt1, c1 = heapq.heappop_max(heap)
            if ans and ans[-1] == c1:
                if not heap:
                    return ""
                cnt2, c2 = heapq.heappop_max(heap)
                cnt2 -= 1
                ans.append(c2)
                if cnt2 > 0:
                    heapq.heappush_max(heap, (cnt2, c2))
            else:
                cnt1 -= 1
                ans.append(c1)
            if cnt1 > 0:
                heapq.heappush_max(heap, (cnt1, c1))
        return "".join(ans)
