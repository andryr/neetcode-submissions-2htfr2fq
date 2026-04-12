class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        flipped = 0
        ans = 0
        cur = 0
        for r in range(len(nums)):
            if nums[r] == 0 and flipped < k:
                flipped += 1
            elif nums[r] == 0:
                while nums[l] != 0:
                    l += 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans