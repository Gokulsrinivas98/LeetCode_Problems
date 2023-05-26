class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def rec_fib(N):
            if N in cache:
                return cache[N]
            if N<2:
                result = N 
            else:
                result = rec_fib(N-1)+rec_fib(N-2)
            
            cache[N] = result
            return result
        return rec_fib(n)
            
            
        