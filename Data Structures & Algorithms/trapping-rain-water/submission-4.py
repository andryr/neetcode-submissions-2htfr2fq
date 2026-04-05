class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_left = [0]
        for h in height:
            if not prefix_left:
                prefix_left.append(h)
            else:
                prefix_left.append(max(h, prefix_left[-1]))
        prefix_left.append(0)
        prefix_right = [0]
        for h in reversed(height):
            if not prefix_right:
                prefix_right.append(h)
            else:
                prefix_right.append(max(h, prefix_right[-1]))
        prefix_right.append(0)
        prefix_right = list(reversed(prefix_right))
        ans = 0
        for i in range(1, len(height) + 1):
            ans += max(0, min(prefix_left[i - 1], prefix_right[i + 1]) - height[i - 1])
        return ans

