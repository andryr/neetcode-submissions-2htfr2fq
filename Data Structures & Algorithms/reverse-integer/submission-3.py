class Solution:
    def reverse(self, x: int) -> int:
        min_int = -2**31
        max_int = 2**31 - 1
        ans = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if ans > max_int // 10 or ans == max_int // 10 and digit > max_int % 10:
                return 0
            if ans < min_int // 10 or ans == min_int // 10 and digit < min_int % 10:
                return 0
            ans = ans * 10 + digit
        return ans
        
