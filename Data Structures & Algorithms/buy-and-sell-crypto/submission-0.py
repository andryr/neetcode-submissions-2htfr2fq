class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix_max = prices[-1]
        ans = 0
        for i in range(len(prices) - 2, -1, -1):
            ans = max(ans, suffix_max - prices[i])
            suffix_max = max(suffix_max, prices[i])
        return ans