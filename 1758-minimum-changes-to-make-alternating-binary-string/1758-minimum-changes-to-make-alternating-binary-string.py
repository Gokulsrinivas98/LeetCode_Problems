class Solution:
    def minOperations(self, s: str) -> int:
        a1=a0=0
        n = len(s)
        for i in range(n):
            b = str(i%2)
            a1 += s[i]!=b
            a0 += s[i]==b
        return min(a1,a0)