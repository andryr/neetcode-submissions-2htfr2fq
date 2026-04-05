class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        steps = 0
        while r < n - 1:
            new_r = r
            for i in range(l, r + 1):
                new_r = max(new_r, i + nums[i])
            steps += 1
            l = r + 1
            r = new_r
        return steps
