class Solution:
    def is_square(self, n):
        sqrt_n = int(math.sqrt(n))
        return sqrt_n * sqrt_n == n

    def numSquares(self, n: int) -> int:
        # If n is a perfect square, return 1.
        if self.is_square(n):
            return 1

        # The result is 4 if and only if n can be written in the 
        # form of 4^k*(8*m + 7). Please refer to 
        # Legendre's three-square theorem.
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4

        # Check whether 2 is the result.
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if self.is_square(n - i * i):
                return 2

        return 3