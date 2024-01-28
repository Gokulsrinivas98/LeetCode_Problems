class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        max_inv = n*(n-1)//2
        if k > max_inv: return 0
        if k == 0 or k == max_inv: return 1
        
        mod = 10**9 + 7
        dp = [[1 if j == 0 else 0 for j in range(k+1)] for i in range(n+1)]
        
        dp[0][0] = 0
        dp[2][1] = 1
        
        for i in range(3,n+1):
            max_inv = min(k,i*(i-1)//2)
            for j in range(1, max_inv + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j >= i :
                    dp[i][j] -= dp[i-1][j-i]
                
        return dp[n][k] % mod
        
