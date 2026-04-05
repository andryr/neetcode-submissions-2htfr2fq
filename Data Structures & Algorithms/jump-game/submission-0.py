class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_idx = [0] * n
        max_idx[0] = nums[0]
        for i in range(1, n):
            if max_idx[i - 1] >= i:
                max_idx[i] = max(max_idx[i - 1], i + nums[i])
        return max_idx[n - 1] >= n - 1
