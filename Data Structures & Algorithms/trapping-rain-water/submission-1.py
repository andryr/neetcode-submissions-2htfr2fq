class Solution:
    def trap(self, height: List[int]) -> int:
        max_hl = height[::]
        for i in range(1, len(height)):
            max_hl[i] = max(max_hl[i - 1], max_hl[i])
        max_hr = height[::]
        for i in range(len(height) - 2, -1, -1):
            max_hr[i] = max(max_hr[i], max_hr[i + 1])
        ans = 0
        for i in range(len(height)):
            ans += min(max_hl[i], max_hr[i]) - height[i]
        return ans