class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        beg = []
        
        ans = 0
        for num in nums:
            if num - 1 in seen:
                continue
            cur = num + 1
            cur_ans = 1
            while cur in seen:
                cur_ans += 1
                cur += 1
            ans = max(ans, cur_ans)
        return ans