class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_set = set()
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            l, r = i + 1, n - 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return ans