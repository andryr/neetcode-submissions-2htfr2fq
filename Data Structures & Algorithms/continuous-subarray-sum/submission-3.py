class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur_sum = 0
        seen_mod = {0: -1}
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum % k in seen_mod:
                if i - seen_mod[cur_sum % k] > 1:
                    return True
            else:
                seen_mod[cur_sum % k] = i
        return False