class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        flipped = 0
        ans = 0
        cur = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                cur += 1
            elif flipped < k:
                flipped += 1
                cur += 1
            else:
                while nums[l] != 0:
                    l += 1
                    cur -= 1
                l += 1
            ans = max(ans, cur)
        return ans