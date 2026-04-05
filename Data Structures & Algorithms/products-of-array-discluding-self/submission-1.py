class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = len([num for num in nums if num == 0])
        if num_zeros > 1:
            return [0] * len(nums)
        sign = 1 if len([num for num in nums if num < 0]) % 2 == 0 else -1
        log_sum = 0
        for num in nums:
            if num != 0:
                log_sum += math.log(abs(num))
        
        return [(1 - num_zeros) * round(math.exp(log_sum - math.log(abs(num))) * sign * math.copysign(1, num)) if num != 0 else round(math.exp(log_sum)) * sign  for num in nums]