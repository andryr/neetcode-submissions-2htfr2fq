class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for c in cnt.values():
            if c == 1:
                return -1
            ans += math.ceil(c / 3)
        return ans