class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_lists = {}
        for u, v, w in edges:
            adj_lists.setdefault(u, []).append((v, w))
        
        ans = {src: 0}
        pq = [(0, src)]
        while pq:
            dist, u = heapq.heappop(pq)
            for v, w in adj_lists.get(u, []):
                if dist + w < ans.get(v, float("inf")):
                    heapq.heappush(pq, (dist + w, v))
                    ans[v] = dist + w
        for i in range(n):
            if i not in ans:
                ans[i] = -1
        return ans

