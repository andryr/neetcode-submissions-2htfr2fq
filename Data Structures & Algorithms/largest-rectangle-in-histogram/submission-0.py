class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()
                ans = max(ans, (i - j) * h)
                start = j
            stack.append((start, height))
        for i, height in stack:
            ans = max(ans, height * (len(heights) - i))
        return ans