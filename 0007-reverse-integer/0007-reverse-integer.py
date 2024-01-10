class Solution:
    def reverse(self, x: int) -> int:
        y = 1
        if x < 0 :
            y = -1
        val = list(str(x*y))
        res = int(''.join(val[::-1]))*y
        
        return res if res > -(2**31) and res < 2**31 - 1 else 0 