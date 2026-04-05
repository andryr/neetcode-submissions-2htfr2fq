class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indices = {c:i for i, c in enumerate(order)}
        s_list = list(s)
        s_list.sort(key=lambda c:indices[c] if c in indices else -1)
        return "".join(s_list)