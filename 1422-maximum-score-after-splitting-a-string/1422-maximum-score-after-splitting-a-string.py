class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        s = list(s)
        m = 0
        for i in range(1,n):
            a = s[:i]
            b = s[i:]
            m = max(m, a.count('0')+b.count('1'))
        return m