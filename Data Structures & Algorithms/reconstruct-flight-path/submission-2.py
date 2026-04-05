class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        visited = set()
        graph = {}
        for a, b in sorted(tickets, reverse=True):
            graph.setdefault(a, []).append(b)

        res = []
        def dfs(src):
            while src in graph and graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
        dfs("JFK")
        return res[::-1]