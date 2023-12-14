class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onerow,onecolumn = [0]*m,[0]*n
        for i in range(m):
            for j in range(n):
                onerow[i] += grid[i][j]
                onecolumn[j] += grid[i][j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*(onerow[i]+onecolumn[j]) - m - n
        return grid
                