class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for chars in zip(*strs):
            if not all(c == chars[0] for c in chars):
                return strs[0][:i]
            i += 1
        return strs[0][:i]