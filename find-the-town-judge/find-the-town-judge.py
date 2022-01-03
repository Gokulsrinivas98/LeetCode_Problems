class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p = [0] * (n+1)
        if n == 1: return 1
        for  i,j in trust:
            p[i] -= 1
            p[j] += 1
        print (p)    
        for i in range(len(p)):
            if p[i] == n-1:
                return i
        return -1    
            
        
        
                