class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0
        while l < r:
            max_l = max(height[l], max_l)
            max_r = max(height[r], max_r)
            if height[l] < height[r]:
                ans += max(0, max_l - height[l])
                l += 1
            else:
                ans += max(0, max_r - height[r])
                r -= 1
        return ans