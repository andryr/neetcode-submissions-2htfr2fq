class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = {"a": a, "b": b, "c": c}
        while sum(cnt.values()) > 0:
            letters = sorted([(cnt[l], l) for l in cnt], reverse=True)
            for remaining, l in letters:
                if remaining > 0 and (len(ans) < 2 or ans[-2:] != [l, l]):
                    ans.append(l)
                    remaining -= 1
                    cnt[l] = remaining
                    break
            else:
                break
        return "".join(ans)