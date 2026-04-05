class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        ans = []
        left, right = 0, 0
        while right < len(s):
            i = left
            while i <= right:
                right = max(right, last_index[s[i]])
                i += 1
            ans.append(right - left + 1)
            left = right + 1
            right = left
        return ans
