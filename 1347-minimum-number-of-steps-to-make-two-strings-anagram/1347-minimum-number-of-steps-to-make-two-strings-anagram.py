class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for i,j in zip(s,t):
            if i not in d : 
                d[i] = 1
            else:
                d[i] += 1
            if j not in d:
                d[j] = -1
            else:
                d[j] -= 1
        c = 0
        for v in d.values():
            if v > 0:
                c += v
        return c
    