# class Solution:
#     def closestPrimes(self, left: int, right: int) -> List[int]:
#         def is_prime(n):
#             if n < 2:
#                 return False
#             i = 2
#             while i*i <= n:
#                 if n % i == 0:
#                     return False
#                 i += 1
#             return True
#         def find_min_diff_elements(list):
#             min_diff = float("inf")
#             min_elements = []
#             for i in range(len(list)):
#                 for j in range(i + 1, len(list)):
#                     diff = abs(list[i] - list[j])
#                     if diff < min_diff:
#                         min_diff = diff
#                         min_elements = [list[i], list[j]]
#             return min_elements

#         primes = []
#         for i in range(left,right+1):
#             if is_prime(i):
#                 primes.append(i)
#         primes.sort()
#         if len(primes) == 2:
#             return primes
#         elif len(primes) < 2:
#             return [-1,-1]
#         else:
#             return find_min_diff_elements(primes)


import math


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for divisor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)
        
        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])
