class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l1 = len(grid)
        l2 = len(grid[0])
        max1 = []
        for i in range(l1-2):
            max1.append([])
            for j in range(l2-2):
                max1[i].append(max(max(grid[k][l] for l in range(j,j+3)) for k in range(i,i+3)))
        return max1