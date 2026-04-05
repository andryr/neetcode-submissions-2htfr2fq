class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            ans = max(cur, ans)
        return ans