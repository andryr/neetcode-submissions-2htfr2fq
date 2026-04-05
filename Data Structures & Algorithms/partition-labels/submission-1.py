class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        
        ans = []
        left, right = 0, 0
        for i, c in enumerate(s):
            right = max(right, last_index[s[i]])

            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans
