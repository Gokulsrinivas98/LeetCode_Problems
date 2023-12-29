class Solution:
    def minDifficulty(self, jD: List[int], d: int) -> int:
        n = len(jD)
        if n < d:
            return -1
        if n == d:
            return sum(jD)
        
        if n < d: return -1
        dp, dp2 = [float('inf')] * n, [0] * n
        for d in range(d):
            stack = []
            for i in range(d, n):
                dp2[i] = dp[i - 1] + jD[i] if i else jD[i]
                while stack and jD[stack[-1]] <= jD[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i], dp2[j] - jD[j] + jD[i])
                if stack:
                    dp2[i] = min(dp2[i], dp2[stack[-1]])
                stack.append(i)
            dp, dp2 = dp2, dp
        return dp[-1]
        
            