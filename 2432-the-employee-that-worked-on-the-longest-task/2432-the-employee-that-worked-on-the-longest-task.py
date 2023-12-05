class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        n = len(logs)
        m = logs[0][1]
        res = logs[0][0]  
        for i in range(1,n):
            t = logs[i][1]-logs[i-1][1]
            if t > m:
                m = t
                res = logs[i][0]
            elif t == m and res > logs[i][0]:
                res = logs[i][0]
        return res