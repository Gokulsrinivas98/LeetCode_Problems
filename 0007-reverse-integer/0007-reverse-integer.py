class Solution:
    def reverse(self, x: int) -> int:
        
        #This code works and is super fast but we should assume we cant store bigger integers thus condition willl fail
#         y = 1
#         if x < 0 :
#             y = -1
#         val = list(str(x*y))
#         res = int(''.join(val[::-1]))*y
        
#         return res if res > -(2**31) and res < 2**31 - 1 else 0 

        max_int = (2**31 - 1)/10
        min_int = (-(2**31))/10
        reverse = 0
        
        while x != 0 :
            if reverse > max_int or reverse < min_int:
                return 0
            dig = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + dig
            x = math.trunc(x/10)
        return reverse
    