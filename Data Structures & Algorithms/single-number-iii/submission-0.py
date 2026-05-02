class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        b = 1
        while not (xor & b):
            b <<= 1
        
        a = 0
        for num in nums:
            if num & b:
                a ^= num

        return [a, xor ^ a]