class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums)
        while l <= r:
            m = (l + r) // 2
            left_neighbour = nums[m - 1] if m > 0 else -float("inf")
            right_neighbour = nums[m + 1] if m < len(nums) - 1 else -float("inf")
            if nums[m] > max(left_neighbour, right_neighbour):
                return m
            if left_neighbour > nums[m]:
                r = m
            else:
                l = m
        