class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_idx = nums[0]
        for i in range(1, n):
            if max_idx >= i:
                max_idx = max(max_idx, i + nums[i])
            
        return max_idx >= n - 1
