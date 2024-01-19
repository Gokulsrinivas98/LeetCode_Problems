class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mini = 2**31
        n = len(matrix)
        if n ==0 : return 0
        if n == 1 : return matrix[0][0]
        for i in range(1,n):
            for j in range(n):
                m = matrix[i-1][j]
                if j-1 >= 0:
                    m = min(m,matrix[i-1][j-1])
                if j+1 < n:
                    m = min(m,matrix[i-1][j+1])
                matrix[i][j] += m
                
                if i == n-1: mini = min(mini,matrix[i][j])
        return mini
            
            