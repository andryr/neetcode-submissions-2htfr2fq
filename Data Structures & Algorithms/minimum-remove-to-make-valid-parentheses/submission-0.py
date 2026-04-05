class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.append(i)
        to_remove = set(stack + to_remove)
        res = [c for i, c in enumerate(s) if i not in to_remove]
        return "".join(res)