class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur = 0
        ans = -float("inf")
        for right in range(2 * n):
            cur += nums[right % n]
            while right - left + 1 > n or (left < right and nums[left % n] < 0):
                cur -= nums[left % n]
                left += 1
            if nums[right % n] > cur:
                cur = nums[right % n]
                left = right
            ans = max(cur, ans)
        return ans
