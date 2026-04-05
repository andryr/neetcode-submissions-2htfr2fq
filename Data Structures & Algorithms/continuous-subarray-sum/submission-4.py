class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_sum = 0
        seen_mod = {0: -1}
        for i, num in enumerate(nums):
            cur_sum += num
            mod = cur_sum % k
            if mod not in seen_mod:
                seen_mod[mod] = i
            elif i - seen_mod[cur_sum % k] > 1:
                return True
        return False