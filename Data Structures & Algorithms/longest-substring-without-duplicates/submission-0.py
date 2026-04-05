class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        ans = 0
        l = 0
        for i, c in enumerate(s):
            l = max(l, last_index.get(c, -1) + 1)
            ans = max(ans, i - l + 1)
            last_index[c] = i
        return ans