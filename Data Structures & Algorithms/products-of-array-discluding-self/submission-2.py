class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = len([num for num in nums if num == 0])
        if num_zeros > 1:
            return [0] * len(nums)
        prefix = 1
        ans = [1]
        for i in range(len(nums) - 1):
            prefix = nums[i] * prefix
            ans.append(prefix)

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans