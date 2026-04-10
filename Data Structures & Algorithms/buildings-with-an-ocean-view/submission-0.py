class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_h = heights[-1]
        ans = [len(heights) - 1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > max_h:
                ans.append(i)
            max_h = max(heights[i], max_h)
        return ans[::-1]