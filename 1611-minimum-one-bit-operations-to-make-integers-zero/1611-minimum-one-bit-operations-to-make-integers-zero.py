class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            print(res)
            n &= n - 1
            print(n)
        return abs(res)