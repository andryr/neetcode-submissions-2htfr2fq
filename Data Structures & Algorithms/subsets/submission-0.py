class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for mask in range(2**n):
            subset = [nums[i] for i in range(n) if mask >> i & 1 == 1]
            ans.append(subset)
        return ans