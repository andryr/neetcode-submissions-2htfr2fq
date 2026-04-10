class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        in_degree = {}
        adj_list = {}
        for a, b in edges:
            adj_list.setdefault(a, []).append(b)
            adj_list.setdefault(b, []).append(a)
            in_degree[a] = in_degree.get(a, 0) + 1
            in_degree[b] = in_degree.get(b, 0) + 1
        queue = deque([a for a in in_degree if in_degree[a] == 1])
        while queue:
            a = queue.popleft()
            in_degree[a] -= 1
            for b in adj_list[a]:
                in_degree[b] -= 1
                if in_degree[b] == 1:
                    queue.append(b)
        for a, b in reversed(edges):
            if in_degree[a] == 2 and in_degree[b] == 2:
                return [a, b]
