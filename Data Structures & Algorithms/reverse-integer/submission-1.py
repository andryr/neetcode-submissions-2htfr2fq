class Solution:
    def reverse(self, x: int) -> int:
        def digits(x):
            return [int(c) for c in str(x) if c.isnumeric()]
        def number(digits):
            return sum(digits[-k - 1] * 10**k for k in range(len(digits)))
        digits_min = digits(-2**31)
        digits_max = digits(2**31 - 1)
        digits_x = list(reversed(digits(x)))
        if x >= 0:
            if len(digits_x) == len(digits_max):
                for dx, dm in zip(digits_x, digits_max):
                    if dx > dm:
                        return 0
                    if dx < dm:
                        break
            return number(digits_x)
        else:
            if len(digits_x) == len(digits_min):
                for dx, dm in zip(digits_x, digits_min):
                    if dx > dm:
                        return 0
                    if dx < dm:
                        break
            return -number(digits_x)
        
