class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                count += dp[i][j]
        return count