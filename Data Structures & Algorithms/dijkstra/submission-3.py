class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_lists = {}
        for u, v, w in edges:
            adj_lists.setdefault(u, []).append((v, w))
        
        ans = {}
        pq = [(0, src)]
        while pq:
            dist, u = heapq.heappop(pq)
            if u in ans:
                continue
            ans[u] = dist
            for v, w in adj_lists.get(u, []):
                if v not in ans:
                    heapq.heappush(pq, (dist + w, v))
        for i in range(n):
            if i not in ans:
                ans[i] = -1
        return ans

