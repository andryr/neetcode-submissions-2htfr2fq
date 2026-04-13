class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for c in cnt.values():
            if c == 1:
                return -1
            if c % 3 == 0:
                ans += c // 3
            elif c % 3 == 2:
                ans += c // 3 + 1
            else:
                ans += (c - 3) // 3 + 2
        return ans