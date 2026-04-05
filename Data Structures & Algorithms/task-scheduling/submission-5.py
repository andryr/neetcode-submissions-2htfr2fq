class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = max(count.values())
        ans = (max_count - 1) * (n + 1) + len([c for c in count.values() if c == max_count])
        return max(ans, len(tasks))