class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_zeros = len([num for num in nums if num == 0])
        if num_zeros > 1:
            return [0] * len(nums)
        for num in nums:
            prod *= num if num != 0 else 1
        print(prod)
        return [(1 - num_zeros) * prod // num if num != 0 else prod for num in nums]