class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, chars in enumerate(zip(*strs)):
            if not all(c == chars[0] for c in chars):
                return strs[0][:i]
        min_len_str = strs[0]
        for s in strs:
            if len(s) < len(min_len_str):
                min_len_str = s
        return min_len_str