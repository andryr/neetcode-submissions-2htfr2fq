class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num_preds = defaultdict(int)
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            num_preds[a] += 1
            adj_list[b].append(a)
        ans = []
        queue = deque([c for c in range(numCourses) if num_preds[c] == 0])
        while queue:
            a = queue.popleft()
            ans.append(a)
            for b in adj_list[a]:
                num_preds[b] -= 1
                if num_preds[b] == 0:
                    queue.append(b)
        if len(ans) < numCourses:
            return []
        return ans