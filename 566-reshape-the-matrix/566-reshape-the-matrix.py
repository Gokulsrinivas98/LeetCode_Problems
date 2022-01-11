class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row,col = len(mat), len(mat[0])
        if row * col != r*c :
            return mat
        reshape = [[0]*c for _ in range(r)]
        for i in range(row * col):
            reshape[i // c][i % c] = mat[i // col][i % col]
        
        return reshape