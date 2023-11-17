class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        r0,r1 = grid[1][n-1],-grid[1][n-1]
        for i in range(n):
            r0 += grid[0][i]
            r1 += grid[1][i]
        score = s0 = s1 = 0
        res = math.inf
        for i in range(n):
            c1 = s1
            c2 = r0 - s0 -grid[1][n-1] - grid[0][i]
            res = min(res,max(c1,c2))
            s0 += grid[0][i]
            s1 += grid[1][i]
        return res
            
              