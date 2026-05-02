class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        num_preds = {}
        for a, b in prerequisites:
            adj.setdefault(a, []).append(b)
            if b not in num_preds:
                num_preds[b] = 1
            else:
                num_preds[b] += 1

        prereqs = {}
        queue = deque([u for u in range(numCourses) if u not in num_preds])
        while queue:
            u = queue.popleft()
            for v in adj.get(u, []):
                if num_preds[v] == 1:
                    queue.append(v)
                prereqs.setdefault(v, set()).add(u)
                prereqs[v].update(prereqs.get(u, []))
                num_preds[v] -= 1

        answer = []
        for u, v in queries:
            answer.append(u in prereqs.get(v, []))

        return answer