class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def rec_subsets(idx, subset):
            if idx >= n:
                ans.append(list(subset))
                return
            subset.append(nums[idx])
            rec_subsets(idx + 1, subset)
            subset.pop()
            rec_subsets(idx + 1, subset)
        rec_subsets(0, [])
        return ans
            
