class Solution:
    def tribonacci(self, n: int) -> int:
        result = [0,1,1]
        for i in range(3,n+1):
            result[i%3] = sum(result)
        return result[n%3]
            