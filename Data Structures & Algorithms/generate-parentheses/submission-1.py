class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(cur, opening, closing):
            if len(cur) == 2 * n:
                if opening == closing:
                    ans.append("".join(cur))
                return
            cur.append("(")
            backtrack(cur, opening + 1, closing)
            cur.pop()
            if closing < opening:
                cur.append(")")
                backtrack(cur, opening, closing + 1)
                cur.pop()
        backtrack([], 0, 0)
        return ans