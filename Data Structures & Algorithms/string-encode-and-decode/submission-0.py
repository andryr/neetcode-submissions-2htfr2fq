class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        read = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                read.append(s[i])
                i += 1
            else:
                l = int("".join(read))
                ss = []
                i += 1
                for j in range(l):
                    ss.append(s[i])
                    i += 1
                ans.append("".join(ss))
                read = []
        return ans